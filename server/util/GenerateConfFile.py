import os


class GenerateConfigurationFile():
    current_dir = os.path.abspath(os.curdir)
    path_to_config_file = os.path.join(current_dir)
    root_path = os.path.normpath(os.getcwd() + os.sep + os.pardir)

    def __init__(self, project_id, remote_path, task_id, source_dir, root_path=root_path):
        self.project_id = project_id
        self.project_checkout_path = os.path.join(root_path, 'projects', str(project_id))
        self.remote_path = remote_path
        self.branch = ''
        self.task_id = task_id
        self.debug = True
        self.source_language = 'en'
        self.source_dir = os.path.join(root_path, 'projects', str(project_id), 'main', source_dir.replace('/', '\\'))
        self.source_match = '\.json$'
        self.translation_file_path = './translations/%LANG%/%LOCALE%.po'

    def write_serge_file(self, current_dir=current_dir, path_to_config_file=path_to_config_file):
        contents = """
        sync
        {
            ts
            {
                plugin                      command

                data
                {
                    project_id               %d
                }
            }

            vcs
            {
                plugin                      git

                data
                {
                    local_path              %s

                    remote_path
                    {
                        main                %s
                    }

                    add_unversioned         YES
                    commit_message          Automatic commit of translation files
                    name                    Transphere
                    email                   johnoula@transphere.com
                }
            }
        }

        jobs
        {
            {
                id                          %s
                name                        Job Test 1
                optimizations               YES
                active                      YES
                debug                       YES
                debug_nosave                NO
                output_only_mode            NO
                source_language             %s
                destination_languages       zh
                source_dir                  %s
                source_process_subdirs      NO
                source_match                %s
                source_exclude_dirs         ^(\.svn|\.git|\.hg|\.bzr|CVS)$
                source_exclude              \.internal\.rc$

                parser
                {
                    plugin                  parse_rc

                    data
                    {
                    }
                }

                serializer
                {
                    plugin                  serialize_po

                    data
                    {
                    }
                }

                normalize_strings           NO
                use_keys_as_context         NO
                leave_untranslated_blank    NO
                db_source                   DBI:SQLite:dbname=./translate.db3
                db_username                 l10n
                db_password                 secretword
                db_namespace                starling
                ts_file_path                %s
                output_lang_files           NO
                output_default_lang_file    NO
                output_encoding             UCS-2LE
                output_bom                  YES

                output_lang_rewrite
                {
                    no                      nb
                }

            }
        }""" % (self.project_id, self.project_checkout_path, self.remote_path, self.task_id, self.source_language,
                self.source_dir, self.source_match, self.translation_file_path)

        try:
            f = open(os.path.join(self.root_path, 'bin', '%s.serge' % self.project_id), 'w+')
            f.write(contents)
            f.close()
        except:
            # os.makedirs(os.path.join(self.root_path, 'bin', str(self.project_id)))
            f = open(os.path.join(self.root_path, 'bin', '%s.serge' % self.project_id), 'w+')
            f.write(contents)
            f.close()


    def write_starling_file(self, access_key, secret_key,):
        ts_path = os.path.join(self.source_dir,"%original_file_name%")
        contents = """
       # Your Starling credentials
# Access Key
"ak": "%s"
# Secret Key
"sk": "%s"
"basePath": "."
"projectId": %d
# download configuration
"download":
  {
    "namespaceId": [  ],
    "taskId": [ ],
    "downloadAllSpaces": true,
    "stringStatus":
      [
        "untranslated",
        "translated",
        "released",
        "unreleased"
      ]
 }
# upload configuration
"upload": {
  "taskId": %d,
#  "targetLanguages": [ "en" ]
}
#
# Files configuration
#
files:
  [
    {
      #
      # Source files filter
      # e.g. "/**/values/*.xml"
      #
      "source": "%s",
      #
      # Where translations will be placed
      #
      "translation": "%s",
      #
      # Files or directories for ignore
      # e.g. ["/**/*.xml"]
      #
      "ignore": [ ]
    }
  ]
       """ % (access_key, secret_key,int(self.project_id),int(self.task_id),self.source_dir.replace('\\','/')+'source.json',ts_path.replace('\\','/'))
        f = open(os.path.join(self.root_path, 'bin','starling.yml'), 'w')
        f.write(contents)
        f.close()

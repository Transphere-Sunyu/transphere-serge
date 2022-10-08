import os

class GenerateConfigurationFile():
    current_dir = os.path.abspath(os.curdir)
    path_to_config_file = os.path.join(current_dir,'serge-1.4','bin')
    checkout_path = os.path.join(current_dir,'serge-1.4','projects')
    def __init__(self, project_Id, remote_path, branch, task_id, source_dir):
        self.project_Id = project_Id
        
        self.remote_path = remote_path
        self.branch = branch if branch else 'main'
        self.task_id = task_id
        self.debug = True
        self.source_language =  'en'
        self.source_dir = source_dir
        self.source_match = '\.json$'
        self.translation_file_path = './translations/%LANG%/%LOCALE%.po'
    
    def write_file(self, checkout_path=checkout_path, path_to_config_file=path_to_config_file):
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
                        main                %s#%s
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
        }""" % (self.project_Id,checkout_path,self.remote_path,self.branch,self.task_id,self.source_language,self.source_dir,self.source_match,self.translation_file_path)
        f = open(path_to_config_file + '/%s.serge' % self.project_Id ,'w' )
        f.write(contents)
        f.close()

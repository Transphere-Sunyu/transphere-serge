package Serge::Sync::Plugin::TranslationService::command;
use parent Serge::Sync::Plugin::Base::TranslationService, Serge::Interface::SysCmdRunner;

use strict;

use Serge::Util qw(subst_macros);

sub name {
    return 'Transphere translation server';
}

sub init {
    my $self = shift;

    $self->SUPER::init(@_);

    $self->{optimizations} = 1; # set to undef to disable optimizations

    $self->merge_schema({
#        project_id => 'STRING',
        executable => 'STRING',
    });
}

sub validate_data {
    my ($self) = @_;

    $self->SUPER::validate_data;

#    $self->{data}->{project_id} = subst_macros($self->{data}->{project_id});
    $self->{data}->{executable} = subst_macros($self->{data}->{executable});

#    $self->{data}->{executable} = 'python' unless defined $self->{data}->{executable};
    $self->{data}->{executable} =  'starling' unless defined $self->{data}->{executable};
#    die "'project_id' not defined" unless defined $self->{data}->{project_id};
}

sub run_manage_py {
    my ($self, $action, $langs, $capture) = @_;

    my $command = $action;

#    if ($langs) {
#        foreach my $lang (sort @$langs) {
#            $lang =~ s/-(\w+)$/'_'.uc($1)/e; # convert e.g. 'pt-br' to 'pt_BR'
#            $command .= " --language=$lang";
#        }
#    }

    $command = $self->{data}->{executable}.' '.$command;
    print "Running '$command'...\n";
    return $self->run_cmd($command, $capture);
}

sub pull_ts {
    my ($self, $langs) = @_;

    my $force = $self->{optimizations} ? '' : ' --overwrite';

    return $self->run_manage_py('client download'.$force, $langs);
}

sub push_ts {
    my ($self, $langs) = @_;

    my $force = $self->{optimizations} ? '' : ' --force';

    $self->run_manage_py("client upload".$force, $langs);
}

1;
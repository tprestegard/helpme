#! /usr/bin/env python3

import textwrap

import click

# TODO:
# tortuga build
# tortuga kit build
# use custom buckets or dev for demo environments
# useful stuff notes
# cloud provider testing
#   rsyncing stuff
#   copying stuff outside of main kit code base (tortuga kit files, listeners, etc.)
# uge commands
# Running django commands in docker compose
# Using custom buckets in cloud bootstrap scripts
# Get signing key for git: gpg --list-secret-keys --keyid-format LONG, take value of "sec" line
# Set default audio device: pactl list short sources pactl set-default-sink, edit /etc/pulse/default.pa


###############################################################################
# Git help ####################################################################
###############################################################################
@click.group()
def git():
    pass

@click.command(name="add-upstream-branch")
def git_add_upstream_branch():
    """Add upstream branch to existing local branch"""
    click.secho("git branch -u origin <branch-name>")


@click.command(name="add-upstream-repo")
def git_add_upstream_repo():
    """Add an upstream repo"""
    click.secho("git remote add upstream <URL>")


@click.command(name="pull-into-another-branch")
def git_pull_into_another_branch():
    """Pull a remote into another local branch without switching branches"""
    click.secho("git fetch origin master:master")
    

@click.command(name="remove-upstream-branch")
def git_remove_upstream_branch():
    """Remove upstream branch from local branch"""
    click.secho("git branch --unset-upstream")


@click.command(name="set-local-repo-as-remote")
def git_set_local_repo_as_remote():
    """Set a git repo on the local filesystem as a remote for another repo"""
    click.secho("git remote add repo_name /path/to/repo.git")


# Git commit
@click.group(name="commit")
def git_commit():
    pass



commit_cmds = (
    (
        "change-author-and-or-date",
        "Change author and/or date of an old commit",
        textwrap.dedent("""
            1. Do an interactive rebase and "edit" the commit
            2. When stopped, do 'git commit --amend --author="name <email>
                                 --date="Tue Dec 12 2017 09:01:14 -0600"'
        """),
    ),
    (
        "remove",
        "Remove a specific commit",
        "git rebase -p --onto SHA1^ SHA1",
    ),
    (
        "set-author-date",
        "Set author date of a commit",
        "git commit -m 'message' --date='Tue Dec 12 2017 09:01:14 -0600'",
    ),
    (
        "set-commit-date",
        "Set commit date of a commit",
        'GIT_COMMITTER_DATE="Tue Dec 12 2017 09:01:14 -0600" git commit ' \
            '-m "message"',
    ),
    (
        "set-author",
        "Set the author of a commit",
        "git commit -m 'message' --author='Name <email>'",
    ),
)

git_cmds = (
    (
        "add-upstream-branch",
        "Add upstream branch to existing local branch",
        "git branch -u origin <branch-name>",
    ),
    (
        "add-upstream-repo",
        "Add an upstream repo",
        "git remote add upstream <URL>",
    ),
    (
        "pull-into-another-branch",
        "Pull a remote into another local branch without switching branches",
        "git fetch origin master:master"
    ),
    (
        "remove-upstream-branch",
        "Remove upstream branch from local branch",
        "git branch --unset-upstream",
    ),
    (
        "set-local-repo-as-remote",
        "Set a git repo on the local filesystem as a remote for another repo",
        "git remote add repo_name /path/to/repo.git",
    ),
    (
        "commit",
        "TBD",
        commit_cmds,
    ),
)

###############################################################################
# cloud #######################################################################
###############################################################################
cloud_cmds = (
    (
        "basic-setup",
        "Basic setup of a cloud server",
        textwrap.dedent("""
            curl https://sdk.cloud.google.com | bash
            # NOTE: select 'yes' when it asks to add to .bashrc
            gcloud init
            exec -l $SHELL
        """),
    ),
)

###############################################################################
# Navops Launch ###############################################################
###############################################################################
bootstrap_cmds = (
    (
        "aws",
        "Bootstrapping AWS demo environment",
        textwrap.dedent("""
            # Setup for specific build
            set -x CUSTOM_BUCKET s3://unicloud-devel/builds/navops-launch/dev-releases/untagged/<build-dir>

            # Setup for latest dev build
            set -x DEV untagged

            # Run script - from root of navops-launch repo
            cd demo
            ./bootstrap-demo-aws.sh
        """),
    ),
    (
        "azure",
        "Bootstrapping Azure demo environment",
        textwrap.dedent("""
            # Setup for specific build
            set -x CUSTOM_BUCKET builds/navops-launch/dev-releases/untagged/<build-dir>

            # Setup for latest dev build
            set -x DEV untagged

            # Run script - from root of navops-launch repo
            cd demo
            ./bootstrap-demo-azure.sh

            # NOTE: make sure to pay attention to the bootstrap process, since
            # it will stop so you can log in to Azure through the browser at
            # some point.
        """),
    ),
    (
        "gcp",
        "Bootstrapping GCP demo environment",
        textwrap.dedent("""
            # Setup for specific build
            set -x CUSTOM_BUCKET gs://navops-build-artifacts/navops-launch/dev-releases/untagged/<build-dir>

            # Setup for latest dev build
            set -x DEV untagged

            # Run script - from root of navops-launch repo
            cd demo
            ./bootstrap-demo-gcp.sh univa-tprestegard
        """),
    ),
)

rsync_cmds = (
    (
        "aws",
        "Rsync to AWS",
        "rsync -av --delete -e \"ssh -i /home/tanner/univa/navops-launch/demo/aws/.ssh/navops-launch-demo-tanner.pem\" . root@ec2-34-213-178-76.us-west-2.compute.amazonaws.com:/root/image_builder/",
    ),
    (
        "azure",
        "Rsync to Azure",
        "rsync -av --delete -e \"ssh -i /home/tanner/univa/navops-launch/demo/azure/.ssh/id_rsa\" . root@52.237.39.219:/root/image_builder/",
    ),
    (
        "gcp",
        "Rsync to GCP",
        "gcp_rsync 35.184.41.31 . /root/image_builder",
    ),
)

navops_launch_cmds = (
    (
        "bootstrap",
        "Running Navops Launch demo environment bootstrap scripts",
        bootstrap_cmds,
    ),
    (
        "rsync",
        "Rsyncing things",
        rsync_cmds,
    ),
)


###############################################################################
# Base command and nesting ####################################################
###############################################################################
@click.group()
def main():
    """
    Help text TBD
    """
    pass


sub_cmds = [
    (
        "git",
        "TBD git help",
        git_cmds,
    ),
    (
        "cloud",
        "TBD cloud help",
        cloud_cmds,
    ),
    (
        "navops-launch",
        "TBD Navops Launch help",
        navops_launch_cmds,
    ),
]


for cmd in sub_cmds:
    main.add_command(recursive_cmd(cmd))


###############################################################################
# __main__ ####################################################################
###############################################################################
if __name__ == '__main__':
    main()

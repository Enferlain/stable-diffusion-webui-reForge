@echo off

set PYTHON=
set GIT=
set VENV_DIR=

@REM ##################################################################
@REM ##                  COMMANDLINE ARGUMENTS                       ##
@REM ##################################################################

set COMMANDLINE_ARGS=--api --theme dark --cuda-malloc --cuda-stream --use-uv

@REM Choose ONE of the following attention optimizations.
@REM SAGE is newer, xformers is the classic choice.
set COMMANDLINE_ARGS=%COMMANDLINE_ARGS% --use-sage-attention
@REM set COMMANDLINE_ARGS=%COMMANDLINE_ARGS% --xformers


echo COMMANDLINE_ARGS is %COMMANDLINE_ARGS%

call webui.bat
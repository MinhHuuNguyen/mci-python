
import os
import argparse


def export_single_file(python_path, html_path, lecture=None):
    if lecture is not None:
        nb_path = os.path.join(python_path, lecture)
        html_name = lecture.split('.')[0]
    else:
        nb_path = python_path
        python_path = '/'.join(python_path.split('/')[:-1])
        html_name = nb_path.split('.')[0].split('/')[-1]

    os.system(f'jupyter nbconvert --to html_embed {nb_path}')

    from_path = os.path.join(python_path, f'{html_name}.html')
    to_path = os.path.join(html_path, f'{html_name}.html')
    os.system(f'mv {from_path} {to_path}')


def export(python_path, html_path):
    if os.path.isdir(python_path):
        os.system(f'rm -rf {args.input}/.ipynb_checkpoints/')
        lectures = sorted(os.listdir(python_path))

        for lecture in lectures:
            if not lecture.endswith('.ipynb'):
                continue

            export_single_file(python_path, html_path, lecture)

    elif os.path.isfile(python_path):
        export_single_file(python_path, html_path)

    else:
        raise f'Invalid input {python_path}'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start inference')
    parser.add_argument('--input', type=str, help='Input ipynb path to export')
    parser.add_argument('--output', type=str, help='Output html path to export')
    args = parser.parse_args()

    export(args.input, args.output)

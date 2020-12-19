# markdown 2 html
import markdown
import os


def main():
    md2htmlPage("index.md","index.html")

    ls = [i[:-3] for i in os.listdir('data_markdown') if i.endswith('.md')]
    for l in ls:
        inf = os.path.join('data_markdown','%s.md'%l)
        outf = os.path.join('data_html','%s.html'%l)
        #print(inf,outf)
        md2htmlPage(inf,outf)

def md2htmlPage(inf,outf):
    try:
        with open(inf, "r", encoding="ansi") as input_file:
            text = input_file.read()
    except:
        with open(inf, "r", encoding='utf-8') as input_file:
            text = input_file.read()
    html = markdown.markdown(text)

    with open(outf, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html)


if __name__ == '__main__':
    main()

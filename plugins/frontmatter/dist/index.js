import matter from "gray-matter"
import remarkFrontmatter from "remark-frontmatter"

export const manifest = {
  name: "frontmatter",
  displayName: "Frontmatter",
  description: "Parse YAML frontmatter for the Digital Nudging Quartz site.",
  version: "1.0.0",
  category: "transformer",
  defaultOrder: 5,
}

function toArray(value) {
  if (value == null) return []
  if (Array.isArray(value)) return value.map(String)
  return String(value)
    .split(/[,\s]+/)
    .map((item) => item.trim())
    .filter(Boolean)
}

function titleFromRelativePath(relativePath) {
  const fileName = String(relativePath ?? "")
    .split("/")
    .pop()
    ?.replace(/\.md$/i, "")
  return fileName || "Untitled"
}

export default function Frontmatter(options = {}) {
  const language = options.language ?? "yaml"
  const delimiters = options.delimiters ?? "---"

  return {
    name: "Frontmatter",
    markdownPlugins() {
      return [
        [remarkFrontmatter, [language]],
        () => {
          return (_tree, file) => {
            const parsed = matter(String(file.value), { delimiters, language })
            const raw = parsed.data ?? {}
            const title = raw.title ?? titleFromRelativePath(file.data.relativePath)
            const aliases = toArray(raw.aliases ?? raw.alias)
            const tags = toArray(raw.tags ?? raw.tag)

            file.data.frontmatter = {
              ...raw,
              title: String(title),
              aliases,
              tags,
              created: raw.created ?? raw.created_on ?? raw.generated_on,
              modified: raw.modified ?? raw.updated ?? raw.updated_on,
              published: raw.published ?? raw.publishDate ?? raw.date,
            }
          }
        },
      ]
    },
  }
}

export { Frontmatter }

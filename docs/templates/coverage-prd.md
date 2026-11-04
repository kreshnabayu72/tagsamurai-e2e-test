# Coverage <Group><SubModul>

Sumber: `<path PRD inti, mis. admin-console/settings-device-sku/PRD/settings-device-sku.md>` · PRD sha256 `<16 hex pertama>` · <N> aturan leaf · <M> spec

<!--
Template halaman coverage alur PRD → E2E (`docs/e2e-conventions-prd.md` bagian 8). Salin ke
`docs/coverage/<Group><SubModul>.md`. Header di atas dibaca `scripts/check-suite-prd.py` (T7, T8): jumlah aturan
leaf dan PRD sha256 diambil dari file rules harness (`e2e-prd rules`). Tabel "Aturan → spec" dan "Spec" diturunkan
script dari frontmatter spec; hanya bagian "Catatan" yang ditulis tangan. Hapus komentar ini di halaman nyata.
-->

## Aturan → spec

| Aturan | Spec | Mode |
|---|---|---|
| `ACDS:V-01` | `TC-AC-ACDS-E2E-003` | FE+BE |

## Di luar E2E

| Aturan | Alasan | Rujukan tc-backend |
|---|---|---|
| `ACDS-LOGIC-06b` | perilaku server murni, tidak teramati di UI | `TC-ACDS-BE-041` |

## Ditahan

| Aturan | Temuan | Catatan |
|---|---|---|
| `ACDS:V-02` | `IGAP-0012` | menunggu keputusan PRD |

## Spec

| Spec | Mode | Langkah | Aturan |
|---|---|---|---|
| `TC-AC-ACDS-E2E-003-register-validasi` | FE+BE | 18 | `ACDS:V-01`, `F-ACDS-02c2` |

## Catatan

- Temuan PRD yang ditemukan saat menulis spec: rujuk temuan `IGAP-…` atau tulis butirnya untuk `prd-internal-gap-check`.

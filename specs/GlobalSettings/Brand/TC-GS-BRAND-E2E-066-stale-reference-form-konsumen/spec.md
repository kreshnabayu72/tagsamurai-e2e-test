---
id: TC-GS-BRAND-E2E-066-stale-reference-form-konsumen
title: "Stale Reference: Submit Form Konsumen dengan Brand yang Baru Dihapus Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-219
  - TC-GS-BRAND-256
  - TC-GS-BRAND-257
coverage:
  web: automated
---

# Stale Reference: Submit Form Konsumen dengan Brand yang Baru Dihapus Admin Lain

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji (spec memakai dua akun UI dan berganti akun secara eksplisit):

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control Client A (Sari Dewi) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | 2 | Total Control (Principal, Hendra Wijaya) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `GS_PRINCIPAL_TC_PASSWORD` |

  Login akun 1 di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (akun 1).
- Admin kedua (hanya lewat API, tanpa login UI):
  - Untuk TC-GS-BRAND-219 dan 257 (Client A): Total Control Client A (admin kedua, Nadia Pratama), `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `GS_TC2_PASSWORD`. Fixture baru (Tabel Data Uji Pre-setup) yang disediakan tim FE.
  - Untuk TC-GS-BRAND-256 (Principal): Tabel Data Uji Pre-setup tidak memuat akun kedua untuk instance Principal, sehingga admin kedua adalah sesi API terpisah atas akun 2 (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, `GS_PRINCIPAL_TC_PASSWORD`), berjalan bersamaan dengan sesi UI akun yang sama. Kemampuan teknis ini dicatat di bawah.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_TC2_PASSWORD` (`GS_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before` (masing-masing oleh akun instance yang bersangkutan), semuanya brand bebas relasi:
  - `Stale Co {runId}-066` (D-28), Client A.
  - `Stale Tag Co {runId}-066` (D-36), Client A.
  - `Stale Dev Co {runId}-066` (D-35), Principal.
- Nilai field wajib lain pada tiga form konsumen (diisi sebelum Submit; Submit ditolak sehingga tidak ada data yang tercipta). Fixture `fixtures/brand.json` belum ada; tim FE menyediakannya:

  | Form | Field | Nilai |
  |---|---|---|
  | Create Asset Name FAMS (`fixed-asset/settings-asset-name` §4.3.1) | Asset Name | `Stale Item {runId}-066` |
  | | Category (kategori daun), TAG Type (minimal 1), UoM | kunci `assetName.category`, `assetName.tagType`, `assetName.uom` |
  | Activate TAG BYO (`global-settings/all-tags` §6.2) | Device Name (dari katalog aktif); SKU dikosongkan | kunci `tagByo.deviceName` |
  | | Identitas TAG (satu baris) | satu identitas dari `tagByo.pool` |
  | Create Device SKU (`admin-console/settings-device-sku`) | Category `BLE Gateway` (tanpa field ekstra), Device Name, SKU | `BLE Gateway`, `Stale Device {runId}-066`, `SKU-ST-{runId}-066` |
  | | Model/Type, Photo (minimal 1) | kunci `deviceSku.modelType`, berkas `fixtures/sampleImage.png` |

- Kemampuan teknis: sesi API terpisah atas akun yang sama dengan sesi UI (akun 2) diizinkan backend; "admin kedua" berupa sesi API yang menghapus brand di antara pilih Brand dan Submit (race antar-aktor); pemicunya langkah eksplisit di spec.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketiga brand bersuffix `{runId}-066` bila masih ada; data lain yang diisi di form tidak disimpan karena Submit ditolak.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-219 dan 257: login sebagai Total Control (Client A). TC-GS-BRAND-256: login sebagai Total Control (Principal).

## Test Steps

### TC-GS-BRAND-219: Submit form konsumen single-select dengan Brand yang baru dihapus

1. Buka form Create Asset Name FAMS (Fixed Asset > Settings > Asset Master > Create Asset Name), pilih Brand `Stale Co {runId}-066`, isi Asset Name `Stale Item {runId}-066`, isi Category, TAG Type, dan UoM dengan nilai dari fixture `assetName`
2. Admin kedua (akun `totalControlSecond_automated_qaTeam1@qwertysystem.net`, lewat API) menghapus `Stale Co {runId}-066`
3. Klik Submit
4. Verifikasi error field `This brand no longer exists. Please select another.`
5. Verifikasi field Brand dikosongkan
6. Buka field Brand
7. Verifikasi opsi Brand di-refresh (`Stale Co {runId}-066` tidak ada di opsi)
8. Verifikasi field lain tetap (nilai yang sudah diisi tidak hilang)
9. Klik `✕` pada form Create Asset Name
10. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
11. Klik `[Leave]`

### TC-GS-BRAND-257: Submit Activate TAG BYO dengan Brand yang baru dihapus

12. Buka Global Settings > All Tags > Activate TAG BYO, pilih Brand `Stale Tag Co {runId}-066`, isi field lain dengan nilai dari fixture `tagByo`
13. Admin kedua (akun `totalControlSecond_automated_qaTeam1@qwertysystem.net`, lewat API) menghapus `Stale Tag Co {runId}-066`
14. Klik Submit
15. Verifikasi error field `This brand no longer exists. Please select another.`
16. Verifikasi field Brand dikosongkan
17. Buka field Brand
18. Verifikasi opsi Brand di-refresh (`Stale Tag Co {runId}-066` tidak ada di opsi)
19. Verifikasi field lain tetap (nilai yang sudah diisi tidak hilang)
20. Klik `✕` pada form Activate TAG BYO
21. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
22. Klik `[Leave]`

### TC-GS-BRAND-256: Submit form Create Device SKU dengan Brand yang baru dihapus

23. Logout, lalu login sebagai Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` dengan `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`
24. Buka Admin Console > Settings > Device SKU, klik `[+ SKU]`, pilih Brand `Stale Dev Co {runId}-066`, isi Category `BLE Gateway`, Device Name `Stale Device {runId}-066`, SKU `SKU-ST-{runId}-066`, serta Model/Type dan Photo dengan nilai dari fixture `deviceSku`
25. Admin kedua (sesi API terpisah atas akun `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`) menghapus `Stale Dev Co {runId}-066`
26. Klik [Submit]
27. Verifikasi error field `This brand no longer exists. Please select another.`
28. Verifikasi field Brand dikosongkan
29. Buka field Brand
30. Verifikasi opsi Brand di-refresh (`Stale Dev Co {runId}-066` tidak ada di opsi)
31. Verifikasi field lain tetap (nilai yang sudah diisi tidak hilang)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sumber: 219 dan 257 (akun Client A) berurutan, lalu 256 (akun Principal) dengan satu kali ganti akun (langkah 23).
- TC-GS-BRAND-219 dan 257 menulis tombol "Submit" tanpa kurung siku, sedangkan TC-GS-BRAND-256 menulis `[Submit]`. Label tombol form Create mengikuti konvensi bagian 9 (`[Submit]`); langkah 3 dan 14 mempertahankan tulisan TC ("Klik Submit").
- Langkah penghubung: langkah 6, 17, dan 29 (membuka field Brand supaya opsi Brand dapat diperiksa pada Verifikasi sesudahnya), serta langkah 9 sampai 11 dan 20 sampai 22 (menutup form dirty lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]`, sebagai pembersihan state antar TC). Verifikasi dialog pada langkah 10 dan 21 adalah asersi tambahan yang tidak ada di TC; ditulis agar penutupan form deterministik (konvensi bagian 10 S-08).
- Tidak ada akun Total Control kedua untuk instance Principal pada Tabel Data Uji Pre-setup TC; admin kedua TC-GS-BRAND-256 memakai sesi API terpisah atas akun yang sama dengan sesi UI; kemampuan teknis itu sudah dicatat sebagai kebutuhan di Prerequisites.
- Nilai field wajib lain ketiga form tidak dirinci di TC sumber; sudah dicatat sebagai kebutuhan di Prerequisites (fixture `fixtures/brand.json` belum ada).

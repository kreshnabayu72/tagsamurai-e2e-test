---
id: TC-FA-LBL-E2E-012-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role
title: "Role Matrix Positif: Aksi Tulis Berhasil Sampai Tuntas per Role (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-34
  - TC-FA-LBL-35
  - TC-FA-LBL-43
coverage:
  web: automated
---

# Role Matrix Positif: Aksi Tulis Berhasil Sampai Tuntas per Role (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Create-Only login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; role lain lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Create-Only | #3 | `Fixture.assetLabeling.akun.createOnly` | `Spectra.env.FA_CREATEONLY_PASSWORD` | TC-FA-LBL-34 | 1 sampai 8 |
| Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` | TC-FA-LBL-35 | 9 sampai 16 |
| Total Control | #1 | `Fixture.assetLabeling.akun.totalControl` | `Spectra.env.FA_LBL_TC_PASSWORD` | TC-FA-LBL-43 | 17 sampai 24 |

- Environment variable: `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Dinamis (Company Alpha, di-seed lewat sesi API di hook `before`, bersuffix `{runId}-012`; label yang dibuat spec lewat UI dan yang tersisa dibersihkan di hook `after`):

| Label | Dipakai di | Kondisi |
|---|---|---|
| `Update Target 35 {runId}-012` | TC-FA-LBL-35 | salinan bersih label katalog (Color default), diubah namanya |
| `TC Baseline 43 {runId}-012` | TC-FA-LBL-43 | bersih, diubah warna lalu dihapus |
| `Create Only Label 34 {runId}-012` | TC-FA-LBL-34 | dibuat spec lewat UI (Color default `#3B82F6`), dibersihkan di `after` |

- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan pembersihan (lihat `suite.md`).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Create-Only: TC-FA-LBL-34

1. Klik `[+ Label]`
2. Isi Label Name dengan `Create Only Label 34 {runId}-012` (Color default)
3. Klik `[Submit]`
4. Verifikasi toast `Success, label has been created.`
5. Verifikasi modal tertutup
6. Ketik Search `Create Only Label 34`, tekan Enter
7. Verifikasi baris `Create Only Label 34 {runId}-012` tampil di Labels List dengan Color Hex `#3B82F6`
8. Verifikasi Total Asset baris `Create Only Label 34 {runId}-012` adalah `0`

### Update-Only: TC-FA-LBL-35

9. Ganti akun: Logout, login sebagai Update-Only `Fixture.assetLabeling.akun.updateOnly` (`Spectra.env.FA_UPDATEONLY_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
10. Ketik Search `Update Target 35`, tekan Enter
11. Klik `⋯` pada baris `Update Target 35 {runId}-012` lalu `Edit`
12. Ubah Label Name menjadi `Update Target 35 Renamed {runId}-012`
13. Klik `[Save]`
14. Verifikasi toast `Success, label has been updated.`
15. Verifikasi modal tertutup
16. Verifikasi baris tampil dengan nama `Update Target 35 Renamed {runId}-012`

### Total Control: TC-FA-LBL-43

17. Ganti akun: Logout, login sebagai Total Control `Fixture.assetLabeling.akun.totalControl` (`Spectra.env.FA_LBL_TC_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
18. Ketik Search `TC Baseline 43`, tekan Enter
19. Klik `⋯` pada baris `TC Baseline 43 {runId}-012` lalu `Edit`, ubah warna menjadi `#10B981`
20. Klik `[Save]`
21. Verifikasi toast `Success, label has been updated.`
22. Klik `⋯` pada baris `TC Baseline 43 {runId}-012` lalu `Delete`
23. Klik `[Delete]` pada dialog
24. Verifikasi toast `Success, label has been deleted.`

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 9 dan 17) karena akun pertama login di hook `before` dan ganti akun menuntut Step eksplisit (bagian 3a, varian A, 2026-10-30).
- Langkah penghubung (S-03): langkah 6, 10, dan 18 (Search untuk menemukan baris target, R-16); langkah 19 menggabungkan dua aksi TC-FA-LBL-43 langkah 1 (buka Edit lalu ubah warna) dalam satu baris tanpa Verifikasi.
- Urutan TC: blok per role supaya tiap akun hanya login sekali; langkah tiap TC tetap mengikuti urutan TC (S-10). Ringkasan: Create-Only, Update-Only, Total Control.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi tidak diasersi: TC-FA-LBL-34 ("label tersimpan", "entri Create tercatat"), TC-FA-LBL-35 ("nama tersimpan").
  - TC-FA-LBL-35 Precondition menyebut label "Pre-setup #12 seed salinan" tanpa menjelaskan salinan atribut apa; spec men-seed label bersih dengan Color default.
  - TC-FA-LBL-34 dan 35 tidak menyebut halaman tempat baris target berada di tabel; Search dipakai sebagai langkah penghubung.

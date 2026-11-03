---
id: TC-FA-LBL-E2E-036-screening-dan-accessibility-popup-edit-label
title: "Screening dan Accessibility Popup Edit Label"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-111
  - TC-FA-LBL-112
coverage:
  web: automated
---

# Screening dan Accessibility Popup Edit Label

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. TC-FA-LBL-112 bertanda UI Only di TC sumber dan berada di spec ini karena memakai layar dan dataset yang sama.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis (label seed milik spec, dibuat lewat fixture BE di hook `before`; Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label; nama bersuffix `{runId}-036`):
  - `Edit Target 111 {runId}-036` (TC-FA-LBL-111)
  - `Edit Target 112 {runId}-036` (TC-FA-LBL-112)
- Data Pre-setup: label `High Priority` (Pre-setup #12) ada di katalog Company Alpha; dipakai TC-FA-LBL-112 hanya sebagai nama duplikat yang diketik dan tidak diubah.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.labelHighPriority` | `High Priority` (Pre-setup #12) |

- Kemampuan teknis: pembacaan atribut `aria-required` dan `aria-describedby` pada field, penekanan tombol Tab berulang, dan pembacaan elemen yang sedang fokus.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus semua label seed milik spec (termasuk yang sudah berganti nama) lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.
- Env var: `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-LBL-111: Screening Popup Edit Label (3 zona) dengan nilai terisi

1. Ketik Search `Edit Target 111 {runId}-036`, tekan Enter
2. Klik `⋯` pada baris `Edit Target 111 {runId}-036`, lalu klik `Edit`
3. Verifikasi Zona Header menampilkan Title `Edit Label` dan tombol Close `[✕]`
4. Verifikasi Zona Body: field Label Name `*` Required berisi `Edit Target 111 {runId}-036`
5. Verifikasi Zona Body: field Color `*` Required dengan Swatch Trigger berlatar `Fixture.assetLabeling.warnaSeed`
6. Verifikasi Zona Body: Live Preview menampilkan chip `Edit Target 111 {runId}-036` berlatar `Fixture.assetLabeling.warnaSeed`
7. Verifikasi Zona Footer menampilkan `[Clear Field]` (Text, Primary) dan `[Save]` (Filled, Success) rata kanan
8. Verifikasi `[Save]` berstatus enabled
9. Verifikasi checkbox `Stay on this form after submitting` dan `[Cancel]` tidak ada di modal
10. Klik icon `[✕]`

### TC-FA-LBL-112: Accessibility Popup Edit Label: aria-required, aria-describedby, focus trap, dan Esc

11. Ganti isi kotak search dengan `Edit Target 112 {runId}-036`, tekan Enter
12. Klik `⋯` pada baris `Edit Target 112 {runId}-036`, lalu klik `Edit`
13. Verifikasi field Label Name dan Color memiliki `aria-required` bernilai true
14. Ganti isi Label Name dengan `Fixture.assetLabeling.labelHighPriority`, tunggu lebih dari 500 ms
15. Verifikasi pesan `Label name already exists` tampil
16. Verifikasi Label Name memiliki `aria-describedby` yang menunjuk pesan error
17. Tekan Tab berulang melewati seluruh elemen yang dapat difokus di dalam modal
18. Verifikasi fokus keyboard terjebak di dalam modal
19. Ganti isi Label Name dengan `Edit Target 112 {runId}-036` (kembalikan ke nilai tersimpan)
20. Tekan Esc
21. Verifikasi modal Edit Label tertutup

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 3b (Edit Label). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 11 adalah Search untuk menemukan baris label target pada Labels List; bukan bagian Expected TC.
- Langkah penghubung (S-03, S-08): langkah 10, 19 menutup modal bersih atau mengembalikan nama ke nilai tersimpan (form tanpa perubahan); Esc pada akhir TC-FA-LBL-112 adalah aksi yang diuji TC (Esc pada form tanpa perubahan menutup modal).
- Seeding minimal (S-11): hanya label yang dipakai langkah `Verifikasi` yang di-seed; nama dasar `Edit Target <nomor TC>` mengikuti TC dan diberi suffix `{runId}-<NNN>` (S-12).
- Temuan untuk QA:
  - TC-FA-LBL-112 langkah 4 hanya menyebut "Tekan Tab berulang" tanpa jumlah tekanan dan tanpa cara mengamati fokus; spec menekan Tab melewati seluruh elemen fokus modal dan memverifikasi fokus tidak keluar modal.
  - TC-FA-LBL-111 Expected c menyebut `[Save]` dan `[Clear Field]` "rata kanan" tanpa nilai ukur; spec mengasersi posisi footer sebagaimana tertulis.

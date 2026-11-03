---
id: TC-FA-COA-E2E-072-defense-in-depth-akses-langsung-atas-akun-terpakai-dan-default-company
title: "Defense-in-Depth: Akses Langsung atas Akun Terpakai dan Default Company, serta Nama Berisi HTML"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-121
  - TC-FA-COA-272
  - TC-FA-COA-273
  - TC-FA-COA-274
  - TC-FA-COA-275
coverage:
  web: automated
---

# Defense-in-Depth: Akses Langsung atas Akun Terpakai dan Default Company, serta Nama Berisi HTML

## Prerequisites

- Mode: FE+BE.
- Kelas harness a (defense-in-depth) untuk TC-FA-COA-272 sampai 275: permintaan langsung ke server tanpa melalui UI; spec hanya mengasersi respons server dan state data (bagian 8b butir 1, `K-1`); asersi absence log tidak ada di spec ini (lihat Notes). TC-FA-COA-121 (nama berisi markup HTML) lewat UI dan diletakkan di spec ini karena sama-sama uji keamanan masukan atas akun; dijalankan pertama.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Permintaan langsung (TC-FA-COA-272 sampai 275) memakai sesi API aktor Total Control (butir "Sesi API aktor" di `suite.md`); tidak ada ganti akun UI.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data Dinamis (D7, dibuat langkah 2 sampai 3 lewat UI, dihapus hook `before` dan `after` lewat API): akun Code `5-6810`, Function Depreciation Expense, Account Name `<b>Test</b> Aset {runId}-072`. Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `5-6810` dibersihkan di hook `before` dan `after` (R-13). Akun tetap Active sampai akhir spec.
- Data Pre-setup yang hanya menjadi target permintaan yang ditolak, tidak diubah (S-06):
  - P6 `5-6002 - Depreciation Expense - Warehouse`: Function Depreciation Expense, Active, Used By 1, belum pernah diekspor (TC-FA-COA-272, 273, 275); fixture Asset Class pemakai disediakan tim FE.
  - P28 `4-7010 - Default Gain - Disposal`: Active, Used By 0, menjadi Default Gain on Disposal (`SET-05`) di Settings > Accounting > Preferences (TC-FA-COA-274); nilai default company diset oleh seed yang disediakan tim FE/BE.
- Data Pre-setup yang diubah satu kali dan dipulihkan: P86 `CAP-8216 - Capitalization Clearing - Direct Bulk Eligible`: Function Capitalization Offset, Active, Used By 0, belum pernah diekspor (TC-FA-COA-275). Langkah 21 menjadikannya Inactive; hook `before` dan `after` memulihkannya ke Active lewat seed idempotent yang disediakan tim FE/BE. Efek pada Last Updated P86 dan entri audit trail dicatat di sini (S-06).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (Deactivate, Delete, Bulk Deactivate) dengan sesi API aktor Total Control; pembacaan akun dari server beserta status dan keberadaannya; hapus akun lewat API untuk cleanup.
- Seed dan pemulihan Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-121: Nama akun berisi markup HTML tampil sebagai teks

1. Klik `+ Account`
2. Isi Account Code `5-6810`, Function Depreciation Expense, Account Name `<b>Test</b> Aset {runId}-072`
3. Klik `[Submit]`
4. Ketik Search `Aset {runId}-072`, tekan Enter
5. Verifikasi di tabel, nama akun tampil sebagai teks literal `<b>Test</b> Aset {runId}-072` (tag tidak hilang diam-diam)
6. Verifikasi nama akun di tabel tidak tampil tebal
7. Klik row action `Edit` pada akun `<b>Test</b> Aset {runId}-072`
8. Verifikasi di modal Edit, Account Name berisi `<b>Test</b> Aset {runId}-072`
9. Verifikasi tidak ada elemen HTML atau script yang dieksekusi pada tabel maupun modal Edit
10. Tutup modal Edit lewat `✕`
11. Klik `(←)` pada kotak Search

### TC-FA-COA-272: Deactivate akun yang dipakai Asset Class

12. Kirim permintaan Deactivate P6 langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
13. Verifikasi permintaan ditolak server dengan penolakan guard Deactivate (`FACO-LOGIC-02c`)
14. Verifikasi status P6 tetap Active pada data dari server

### TC-FA-COA-273: Delete akun yang dipakai Asset Class

15. Kirim permintaan Delete P6 langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
16. Verifikasi permintaan ditolak server dengan penolakan Guard 2 (`FACO-LOGIC-03`)
17. Verifikasi akun P6 tetap ada pada data dari server

### TC-FA-COA-274: Delete akun nilai default company

18. Kirim permintaan Delete P28 langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
19. Verifikasi permintaan ditolak server
20. Verifikasi akun P28 tetap ada pada data dari server

### TC-FA-COA-275: Bulk Deactivate campuran akun terpakai dan akun eligible

21. Kirim permintaan Bulk Deactivate untuk P6 dan P86 langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
22. Verifikasi status P6 tetap Active pada data dari server
23. Verifikasi akun P86 menjadi Inactive pada data dari server

## Notes

- `K-1`: TC-FA-COA-272, 273, 274, dan 275 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan kontrak API, karena TC granular tetap sumber.
- TC-FA-COA-121 adalah satu-satunya blok UI; ditempatkan di spec ini dan dijalankan pertama sebelum blok permintaan langsung.
- Langkah penghubung (S-03, R-16, R-23): langkah 4 (Search nama akun untuk menemukan baris target di tabel yang dapat memuat lebih dari satu halaman), langkah 10 (menutup modal Edit tanpa perubahan, form tidak dirty), langkah 11 (mengembalikan kotak Search ke keadaan awal).
- Klausa "tidak ada log" pada Expected TC-FA-COA-275 a ("tidak ada log untuk P6") dan Post Condition TC-FA-COA-272, 273, 274, 275 tidak diasersi di spec ini (S-05); belum ada spec absence yang memuatnya (lihat Temuan untuk QA).
- Langkah 21 sampai 23 berada di akhir spec karena mengubah state (P86 menjadi Inactive).
- Temuan untuk QA:
  - TC-FA-COA-274 dan 275 hanya menyebut "ditolak server" tanpa kode status; spec tidak mengasersi kode tertentu. TC-FA-COA-272 dan 273 menyebut guard (`FACO-LOGIC-02c`, `FACO-LOGIC-03`) tanpa kode status.
  - TC-FA-COA-275 Expected b "Akun P86 menjadi Inactive" dan a "tidak ada log untuk P6" mencampur state dan absence log; klausa log belum dimiliki spec absence mana pun.
  - TC-FA-COA-121 tidak menyebut toast sukses sesudah `[Submit]`; spec tidak mengasersinya. Post Condition "Akun tersimpan dengan Account Name yang tampil seperti di langkah 3" tidak punya langkah observasi terpisah selain Expected a dan b; tidak diasersi tersendiri (S-01).
  - TC-FA-COA-121 memakai Account Name `<b>Test</b> Aset` tanpa suffix; spec menambah suffix `{runId}-072` pada nama (S-12) dan Code literal `5-6810` dibersihkan di hook.
  - TC-FA-COA-121 berkelas Security tetapi berjalur UI, sehingga bukan defense-in-depth (kelas a); ditempatkan di spec ini menurut pengelompokan tema keamanan akun.
  - Nilai default company P28 (`SET-05`) tidak punya identitas fixture di TC; disediakan tim FE/BE.

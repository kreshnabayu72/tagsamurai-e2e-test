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
- Data Dinamis (D7, dibuat langkah 2 sampai 3 lewat UI, dihapus hook `before` dan `after` lewat API): akun Code `5-6810`, Function Depreciation Expense, Account Name `<b>Test</b> Aset {runId}-072`. Akun tetap Active sampai akhir spec.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE):
  - Akun dipakai Asset Class: Code `DID072A`, Account Name `Akun Dipakai {runId}-072`, Function Depreciation Expense, Active, Used By 1 oleh Asset Class `Asset Class Pemakai {runId}-072` yang dibuat hook `before` dan dihapus hook `after`; belum pernah diekspor; padanan P6 pada TC-FA-COA-272, 273, dan 275. Semua permintaan atas akun ini ditolak sehingga tidak berubah.
  - Akun default company: Code `DID072B`, Account Name `Akun Default Gain {runId}-072`, Function Gain on Disposal, Active, Used By 0; menjadi Default Gain on Disposal (`SET-05`) di Settings > Accounting > Preferences; padanan P28 pada TC-FA-COA-274. Permintaan Delete atas akun ini ditolak sehingga tidak berubah.
  - Akun eligible: Code `DID072C`, Account Name `Akun Eligible {runId}-072`, Function Capitalization Offset, Active, Used By 0, belum pernah diekspor; padanan P86 pada TC-FA-COA-275. Langkah 21 menjadikannya Inactive.
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID072A`, `DID072B`, `DID072C` memuat nomor spec supaya unik per spec, sedangkan `5-6810` adalah nilai TC. Keempat Code dibersihkan di hook `before` dan `after` (R-13).
- State global: spec mengubah nilai Default Gain on Disposal di Settings > Accounting > Preferences menjadi `DID072B`. Hook `before` menyimpan nilai awal dan menyetel `DID072B` sebagai default, hook `after` memulihkan nilai awal sebelum menghapus `DID072B` (R-08). Kemampuan menyetel dan memulihkan nilai default company disediakan tim FE/BE; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): klien HTTP untuk permintaan langsung (Deactivate, Delete, Bulk Deactivate) dengan sesi API aktor Total Control; pembacaan akun dari server beserta status dan keberadaannya; hapus akun lewat API untuk cleanup.
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`. Suite berjalan serial (`parallel: false`).

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

12. Kirim permintaan Deactivate `DID072A` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
13. Verifikasi permintaan ditolak server dengan penolakan guard Deactivate (`FACO-LOGIC-02c`)
14. Verifikasi status `DID072A` tetap Active pada data dari server

### TC-FA-COA-273: Delete akun yang dipakai Asset Class

15. Kirim permintaan Delete `DID072A` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
16. Verifikasi permintaan ditolak server dengan penolakan Guard 2 (`FACO-LOGIC-03`)
17. Verifikasi akun `DID072A` tetap ada pada data dari server

### TC-FA-COA-274: Delete akun nilai default company

18. Kirim permintaan Delete `DID072B` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
19. Verifikasi permintaan ditolak server
20. Verifikasi akun `DID072B` tetap ada pada data dari server

### TC-FA-COA-275: Bulk Deactivate campuran akun terpakai dan akun eligible

21. Kirim permintaan Bulk Deactivate untuk `DID072A` dan `DID072C` langsung ke server menggunakan sesi API aktor Total Control hingga respons diterima
22. Verifikasi status `DID072A` tetap Active pada data dari server
23. Verifikasi akun `DID072C` menjadi Inactive pada data dari server

## Notes

- `K-1`: TC-FA-COA-272, 273, 274, dan 275 berkelas a dengan Expected respons API; tetap di spec FE+BE walau tumpang tindih dengan kontrak API, karena TC granular tetap sumber.
- TC-FA-COA-121 adalah satu-satunya blok UI; ditempatkan di spec ini dan dijalankan pertama sebelum blok permintaan langsung.
- Pembagian TC lintas spec (S-05): klausa "tidak ada log" pada Expected TC-FA-COA-275 a dan Post Condition TC-FA-COA-272, TC-FA-COA-273, TC-FA-COA-274, dan TC-FA-COA-275 diasersi di spec 096 (TC-FA-COA-272) dan spec 097 (TC-FA-COA-273, 274, 275), yang memuat permintaan langsung yang sama dengan baseline sendiri. Spec ini hanya mengasersi respons server dan state data.
- Target aksi memakai akun milik spec (S-06): TC memakai P6, P28, dan P86, spec memakai `DID072A`, `DID072B`, dan `DID072C` dengan state yang sama.
- Langkah penghubung (S-03, R-16, R-23): langkah 4 (Search nama akun untuk menemukan baris target di tabel yang dapat memuat lebih dari satu halaman), langkah 10 (menutup modal Edit tanpa perubahan, form tidak dirty), langkah 11 (mengembalikan kotak Search ke keadaan awal).
- Langkah 21 sampai 23 berada di akhir spec karena mengubah state (`DID072C` menjadi Inactive).
- Temuan untuk QA:
  - TC-FA-COA-274 dan 275 hanya menyebut "ditolak server" tanpa kode status; spec tidak mengasersi kode tertentu. TC-FA-COA-272 dan 273 menyebut guard (`FACO-LOGIC-02c`, `FACO-LOGIC-03`) tanpa kode status.
  - TC-FA-COA-275 Expected b "Akun P86 menjadi Inactive" dan a "tidak ada log untuk P6" mencampur state dan absence log; klausa log diasersi di spec 097.
  - TC-FA-COA-121 tidak menyebut toast sukses sesudah `[Submit]`; spec tidak mengasersinya. Post Condition "Akun tersimpan dengan Account Name yang tampil seperti di langkah 3" tidak punya langkah observasi terpisah selain Expected a dan b; tidak diasersi tersendiri (S-01).
  - TC-FA-COA-121 memakai Account Name `<b>Test</b> Aset` tanpa suffix; spec menambah suffix `{runId}-072` pada nama (S-12) dan Code literal `5-6810` dibersihkan di hook.
  - TC-FA-COA-121 berkelas Security tetapi berjalur UI, sehingga bukan defense-in-depth (kelas a); ditempatkan di spec ini menurut pengelompokan tema keamanan akun.
  - Menyetel akun milik spec sebagai nilai default company (`SET-05`) mengubah state global Preferences; perlu dikonfirmasi tim FE/BE bahwa nilai itu dapat disetel dan dipulihkan lewat seed.

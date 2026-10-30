---
id: TC-GS-UCF-E2E-029-multi-konteks-create-bersamaan
title: "Multi-Konteks: Create Bersamaan Field Name Sama oleh Dua Admin dan Dua Admin Berebut Slot Terakhir Master Data Count Limit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-323
  - TC-GS-UCF-89
coverage:
  web: automated
---

# Multi-Konteks: Create Bersamaan Field Name Sama oleh Dua Admin dan Dua Admin Berebut Slot Terakhir Master Data Count Limit

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`): TC-GS-UCF-89 memakai volume 999 field dan Master Data Count Limit 1.000 pada entitas Client Limit yang diatur backend dan dipulihkan setelah spec.
- Akun (password hanya lewat env var, tidak ditulis di spec atau fixture):
  - Client A, Sesi A: Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`.
  - Client A, Sesi B: Total Control Client A admin kedua (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`. Login di hook `before` pada konteks browser terpisah.
  - Client Limit, Sesi A: Total Control Client Limit (Wulan Sari) `totalControl_automated_qaTeam4@qwertysystem.net`, `Spectra.env.GS_LIMIT_TC_PASSWORD`. Dipakai TC-GS-UCF-89 lewat langkah ganti akun eksplisit.
  - Client Limit, Sesi B: Total Control Client Limit admin kedua (Yoga Permana) `totalControlSecond_automated_qaTeam4@qwertysystem.net`, `Spectra.env.GS_LIMIT_TC2_PASSWORD`. Dipakai TC-GS-UCF-89 lewat langkah ganti akun eksplisit.
  - Hook `after` menutup konteks Sesi B, serta mengembalikan sesi ke akun default suite.
- Dua sesi browser paralel pada Global Settings > User > Custom Field (kelas multi-konteks, dua admin).
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach` di kedua sesi; blok Client Limit membukanya lewat langkah eksplisit sesudah ganti akun.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk setiap akun aktor spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Data Dinamis milik spec (nama bersuffix `{runId}-029`; fixture baru `Fixture.customFieldUser.createRace029`; tidak di-seed, dibuat oleh aksi uji; Text, Required No): `Same Name {runId}-029` (TC-GS-UCF-323), `Slot A {runId}-029` dan `Slot B {runId}-029` (TC-GS-UCF-89).
- Data Pre-setup Client Limit untuk TC-GS-UCF-89: tepat 999 Custom Field (fixture backend `Lim 001` sampai `Lim 999`), Master Data Count Limit 1.000; volume diatur backend sebelum blok ("disediakan tim BE").
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-029` pada Client A dan Client Limit; pulihkan volume Client Limit ke nilai awal (disediakan tim BE); tutup konteks Sesi B.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`; klik `[Submit]` pada dua sesi "hampir bersamaan" (TC-GS-UCF-89).
- State global yang diubah: volume Custom Field entitas Client Limit (dipulihkan seperti di atas); flag Guided Tooltip dikelola hook suite.

## Test Steps

### TC-GS-UCF-323: Dua admin membuat Field Name yang sama bersamaan

1. [Sesi A] Klik `[+ Custom Field]`, isi Field Name `Same Name {runId}-029`, Data Type `Text`
2. [Sesi B] Klik `[+ Custom Field]`, isi Field Name `Same Name {runId}-029`, Data Type `Text`
3. [Sesi A] Klik `[Submit]`
4. [Sesi A] Verifikasi toast sukses: "Success, custom field has been created."
5. [Sesi B] Klik `[Submit]`
6. [Sesi B] Verifikasi error inline `Field name already exists`
7. [Sesi B] Verifikasi form tetap terbuka
8. [Sesi B] Klik `[✕]`
9. [Sesi B] Verifikasi dialog `Unsaved Changes` tampil
10. [Sesi B] Klik `[Leave]`

### TC-GS-UCF-89: Dua admin berebut slot terakhir Master Data Count Limit

11. Ganti akun: Sesi A logout lalu login sebagai Total Control Client Limit (Wulan Sari); Sesi B logout lalu login sebagai Total Control Client Limit admin kedua (Yoga Permana); keduanya membuka Global Settings > User > Custom Field
12. Atur backend: limit 1.000 dan tepat 999 Custom Field, lalu muat ulang halaman di kedua sesi
13. [Sesi A] Klik `[+ Custom Field]`, isi Field Name `Slot A {runId}-029`, Data Type `Text`
14. [Sesi B] Klik `[+ Custom Field]`, isi Field Name `Slot B {runId}-029`, Data Type `Text`
15. [Sesi A dan Sesi B] Klik `[Submit]` hampir bersamaan
16. Verifikasi tepat satu sesi (pemenang) mendapat toast sukses: "Success, custom field has been created."
17. Verifikasi sesi lain (yang kalah) mendapat Dialog `Limit Reached` dengan body `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.`
18. Verifikasi sesi yang kalah tidak menampilkan pesan duplikat (tidak ada error inline `Field name already exists`)
19. Verifikasi form tetap terbuka pada sesi yang kalah
20. [Sesi yang kalah] Klik `[OK]`, klik `[✕]`
21. [Sesi yang kalah] Verifikasi dialog `Unsaved Changes` tampil
22. [Sesi yang kalah] Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas harness: multi-konteks (dua admin), bagian 3 prinsip 13c. Spec serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kedua TC adalah satu topik: balapan Submit Create oleh dua admin (nama yang sama pada Client A, dan slot terakhir limit pada Client Limit), keduanya dengan harness dua sesi browser. Blok entitas Client Limit berurutan sesudah blok Client A dengan langkah ganti akun eksplisit, dan tiap blok mengatur datanya sendiri (nama bersuffix) sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Urutan TC: TC-GS-UCF-323 (Client A) lebih dulu, TC-GS-UCF-89 (Client Limit, volume khusus) paling akhir. Urutan berbeda dari TC sumber (89, 323).
- Langkah penghubung (aksi tanpa `Verifikasi`): mengisi form pada dua sesi sebelum `[Submit]`, ganti akun, "Atur backend ..." (pengaturan volume oleh tim BE), memuat ulang halaman, klik `[OK]`, serta menutup form dirty lewat `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]` (S-08).
- Pada TC-GS-UCF-323 `[Submit]` Sesi A dan Sesi B dilakukan berurutan sesuai langkah TC ("A klik [Submit], lalu B klik [Submit]"); pada TC-GS-UCF-89 pemenang tidak ditentukan sehingga asersi ditulis atas "sesi pemenang" dan "sesi yang kalah".
- Pembagian TC lintas spec: TC-GS-UCF-324 (submit ganda dua tab) ada di spec 076; TC-GS-UCF-87, 88, 90, 302, 364, 435, 453 (Master Data Count Limit Create) ada di spec 027 dan TC-GS-UCF-454 ada di spec 028.
- Temuan untuk QA:
  - TC-GS-UCF-89 dan 323 bertanda Manual Only (d) karena dua sesi paralel; kebutuhannya (dua konteks browser) ditulis di Prerequisites sesuai konvensi bagian 2. Kedua sesi sama-sama diasersi (toast sukses, error inline, Dialog `Limit Reached`) sehingga keduanya sesi UI, bukan sesi API pemicu.
  - TC-GS-UCF-89: Data Uji `Slot A; Slot B` tanpa menyatakan siapa pemenang; asersi ditulis atas pemenang dan yang kalah. Volume 999 field diatur backend; admin kedua (Yoga Permana) bukan akun Pre-setup yang disebut password-nya di TC (env `GS_LIMIT_TC2_PASSWORD` mengikuti `.env.example`).
  - TC-GS-UCF-323: Post Condition "Same Name (Same Name (D-101))" tanpa langkah observasi tambahan; tidak diasersi di luar Expected.
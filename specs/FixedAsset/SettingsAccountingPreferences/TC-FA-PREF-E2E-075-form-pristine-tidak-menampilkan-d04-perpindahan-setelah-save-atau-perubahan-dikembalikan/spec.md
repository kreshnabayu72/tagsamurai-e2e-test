---
id: TC-FA-PREF-E2E-075-form-pristine-tidak-menampilkan-d04-perpindahan-setelah-save-atau-perubahan-dikembalikan
title: "Form Pristine Tidak Menampilkan D-04; Perpindahan Setelah Save atau Setelah Perubahan Dikembalikan Tidak Menampilkan Dialog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-266
  - TC-FA-PREF-267
  - TC-FA-PREF-268
  - TC-FA-PREF-269
  - TC-FA-PREF-576
coverage:
  web: automated
---

# Form Pristine Tidak Menampilkan D-04; Perpindahan Setelah Save atau Setelah Perubahan Dikembalikan Tidak Menampilkan Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: TC-266 sampai 269 memakai PB-1 dan PB-2 (akun Chart of Accounts tersedia); TC-576 memakai PC-1. Nilai awal PB-1 dan PC-1 setara (In-service Date Source "Activation date").
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini menyimpan In-service Date Source "Manual by Accounting" pada TC-269; pemulihan ke nilai awal dilakukan pada langkah 22 dan di hook `after` spec ini.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-266: Berpindah tab dengan form pristine tidak menampilkan dialog

1. Klik tab Chart of Accounts pada Settings > Accounting
2. Verifikasi tidak ada dialog yang tampil
3. Verifikasi tab Chart of Accounts aktif
4. Klik tab Preferences pada Settings > Accounting

### TC-FA-PREF-267: Berpindah lewat sidebar dengan form pristine tidak menampilkan dialog

5. Klik salah satu entri menu sidebar selain Accounting
6. Verifikasi tidak ada dialog yang tampil
7. Verifikasi halaman entri sidebar yang diklik tampil
8. Buka kembali Settings > Accounting > Preferences

### TC-FA-PREF-268: Berpindah tab setelah perubahan dikembalikan ke nilai tersimpan tidak menampilkan dialog

9. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
10. Ubah kembali Select In-service Date Source menjadi "Activation date"
11. Verifikasi [Save changes] dan [Cancel] berstatus Disabled setelah nilai dikembalikan
12. Klik tab Chart of Accounts pada Settings > Accounting
13. Verifikasi tidak ada dialog yang tampil
14. Verifikasi tab Chart of Accounts aktif
15. Klik tab Preferences pada Settings > Accounting

### TC-FA-PREF-269: Berpindah tab sesudah Save berhasil tidak menampilkan dialog

16. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
17. Klik [Save changes]
18. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
19. Klik tab Chart of Accounts pada Settings > Accounting
20. Verifikasi tidak ada dialog D-04 saat berpindah tab
21. Verifikasi tab Chart of Accounts aktif
22. Seed ulang Preferences ke PC-1 lewat API (In-service Date Source "Activation date") dan buka kembali Fixed Asset > Settings > Accounting > Preferences
23. Verifikasi Select In-service Date Source menampilkan "Activation date" sebagai bukti pemulihan nilai awal

### TC-FA-PREF-576: Meninggalkan halaman dengan form pristine tidak menampilkan dialog

24. Klik entri sidebar menu lain tanpa mengubah form
25. Verifikasi tidak ada dialog apa pun yang tampil
26. Verifikasi halaman menu lain terbuka

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 4, 8, 15 (kembali ke tab Preferences agar TC berikutnya mulai dari layar awal), langkah 22 dan 23 (seed ulang dan pemulihan nilai awal sebelum TC-576 yang memakai seri PC-1; langkah 23 memverifikasi hasil pemulihan).
- Post Condition TC-269 ("Preferences company menyimpan In-service Date Source = Manual by Accounting") tidak diasersi terpisah setelah Save; nilai tersimpan tercermin pada toast sukses (langkah 18). TC-266, 267, 268 dan 576 tidak mengubah nilai tersimpan.
- Temuan untuk QA:
  - TC-FA-PREF-269 memuat Post Condition "tersimpan Manual by Accounting" tetapi Expected tidak meminta pembacaan ulang nilai tersimpan; spec tidak menambah asersi pembacaan.
  - TC-FA-PREF-266 dan 267 menyebut "salah satu entri menu sidebar" tanpa nama entri; spec memilih entri apa pun selain Accounting.

---
id: TC-GS-NLU-E2E-016-create-validasi-batas-120-karakter-dan-batas-tepat-120
title: "Create: validasi batas 120 karakter dan batas tepat 120"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-66
  - TC-GS-NLU-67
coverage:
  web: automated
---

# Create: validasi batas 120 karakter dan batas tepat 120

## Prerequisites

- Mode: FE+BE (backend nyata; validasi server dan state tabel dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Division `Operations`, Login User `Ahmad Fauzi` (pool Represented By).
- Data Dinamis TC-GS-NLU-67 (record tersimpan): First Name 120 karakter `a`, Last Name 120 karakter `b`; Employee ID 120 karakter `c` dan Email 120 karakter yang keduanya dihitung termasuk suffix per run: Employee ID = `c` × (120 − panjang `-{runId}-016`) + `-{runId}-016`; Email = `d` × n + `+{runId}-016@test.com` dengan total tepat 120 karakter. First Name dan Last Name tidak butuh suffix (tidak unik). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-016@test.com` lewat API (mekanisme disediakan tim FE/BE).
- Data TC-GS-NLU-66 (tidak tersimpan): First Name, Last Name, Employee ID masing-masing 121 karakter `a`; Email 121 karakter (`a` × 112 + `@test.com`).
- Kemampuan teknis: membaca jumlah total baris tabel (baseline B0).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-66: Validasi batas 120 karakter

1. Catat jumlah total baris tabel Non-Login User sebagai baseline B0
2. Klik `[+ Non-Login User]`
3. Isi First Name dengan 121 karakter `a`
4. Isi Last Name dengan 121 karakter `a`
5. Isi Employee ID dengan 121 karakter `a`
6. Isi Email dengan 121 karakter (`a` × 112 + `@test.com`)
7. Pilih Division `Operations` dan Represented By `Ahmad Fauzi` (klik `[+ Select User]`, klik baris `Ahmad Fauzi`, klik `[Select]`)
8. Klik `[Submit]`
9. Verifikasi First Name: pesan inline `Max. 120 characters`
10. Verifikasi Last Name: pesan inline `Max. 120 characters`
11. Verifikasi Employee ID: pesan inline `Max. 120 characters`
12. Verifikasi Email: pesan inline `Max. 120 characters`
13. Verifikasi Popup Create tetap terbuka
14. Verifikasi tidak ada toast sukses
15. Verifikasi jumlah total baris tabel sama dengan baseline B0
16. Verifikasi keempat pesan `Max. 120 characters` tetap tampil

### TC-GS-NLU-67: Batas tepat 120 karakter diterima

17. Klik `[Clear Field]`
18. Isi First Name dengan 120 karakter `a`
19. Isi Last Name dengan 120 karakter `b`
20. Isi Employee ID dengan 120 karakter `c` (termasuk suffix)
21. Isi Email dengan 120 karakter valid (`d` × n + `+{runId}-016@test.com`)
22. Pilih Division `Logistics` dan Represented By `Ahmad Fauzi` (klik `[+ Select User]`, klik baris `Ahmad Fauzi`, klik `[Select]`)
23. Klik `[Submit]`
24. Verifikasi tidak ada pesan `Max. 120 characters` pada First Name, Last Name, Employee ID, dan Email
25. Verifikasi toast sukses `Success, non-login user has been created.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Validasi diblokir (TC-GS-NLU-66) mendahului aksi sukses (TC-GS-NLU-67; S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline B0 untuk klausa "tidak ada record baru di tabel" TC-GS-NLU-66 Expected e, dibaca pada tabel di belakang Popup dan diasersi di langkah 15), langkah 17 (`[Clear Field]` agar pesan TC-GS-NLU-66 dan isian tidak terbawa).
- Langkah 9 sampai 16 memetakan lima klausa Expected a sampai e TC-GS-NLU-66 (Expected e dipecah menjadi langkah 13, 14, 15, dan 16).
- Pada langkah 22 TC-GS-NLU-67 memakai Division `Logistics` karena TC menulis "isi `Logistics` dan `Ahmad Fauzi` bila kosong" dan `[Clear Field]` di langkah 17 mengosongkannya.
- Temuan untuk QA:
  - TC-GS-NLU-67 menyebut Email 120 karakter bertipe `d` × 111 + `@test.com` dan Employee ID 120 karakter `c`; spec menghitung 120 karakter termasuk suffix `{runId}` (R-06) sehingga jumlah karakter `d` dan `c` lebih sedikit dari TC.
  - TC-GS-NLU-67 Expected b hanya menyebut toast sukses (record tidak diasersi di tabel); spec tidak menambah asersi record.

---
id: TC-GS-NLU-E2E-024-create-field-phone-country-code-dan-number
title: "Create: field Phone Country Code dan Number"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-502
  - TC-GS-NLU-503
  - TC-GS-NLU-504
coverage:
  web: automated
---

# Create: field Phone Country Code dan Number

## Prerequisites

- Mode: FE+BE (backend nyata; validasi Number berjalan di browser, Create dan Detail dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9, 10, dan 13, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By), Custom Field aktif `Emergency Phone` (Phone, tidak Required).
- Data Dinamis milik spec: Non-Login User `Rani Wijaya {runId}-024` (First Name `Rani`, Last Name `Wijaya {runId}-024`), Email `raniwijaya+{runId}-024@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-024` lewat API (mekanisme disediakan tim FE/BE).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-502: Country Code default dan dropdown Country Code

1. Klik `[+ Non-Login User]`
2. Verifikasi Country Code Emergency Phone terpilih `🇮🇩 +62`
3. Verifikasi Number Emergency Phone kosong
4. Buka dropdown Country Code Emergency Phone
5. Verifikasi dropdown Country Code searchable dan memuat kode panggilan negara dari katalog
6. Verifikasi dropdown Country Code tidak memuat opsi kosong
7. Tutup dropdown tanpa memilih opsi lain
8. Verifikasi Country Code tetap `🇮🇩 +62`

### TC-GS-NLU-503: Validasi Number Phone real-time

9. Ketik `a1b2` pada Number Emergency Phone
10. Verifikasi Number berisi `12` (huruf tidak masuk, tanpa pesan)
11. Verifikasi error inline `Min. 4 characters` tampil langsung
12. Kosongkan Number, lalu ketik `1234567890123456` (16 digit)
13. Verifikasi error inline `Max. 15 characters` tampil pada digit ke-16
14. Hapus satu digit terakhir sehingga Number berisi 15 digit (`123456789012345`)
15. Verifikasi tidak ada error inline pada Number

### TC-GS-NLU-504: Phone non-Required dengan Number kosong diterima

16. Kosongkan Number Emergency Phone dengan Country Code tetap `🇮🇩 +62`
17. Isi First Name `Rani`, Last Name `Wijaya {runId}-024`, dan Email `raniwijaya+{runId}-024@qwertysystem.net`
18. Pilih Division `Logistics`
19. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
20. Verifikasi tidak ada error inline pada Emergency Phone
21. Klik `[Submit]`
22. Verifikasi toast sukses `Success, non-login user has been created.`
23. Ketik Search `Rani Wijaya {runId}-024`, tekan Enter
24. Verifikasi `Rani Wijaya {runId}-024` tampil di list
25. Buka Detail record `Rani Wijaya {runId}-024` dan perluas bagian Custom Fields
26. Verifikasi Emergency Phone menampilkan `—`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-NLU-502 dan TC-GS-NLU-503 tidak submit dan memakai satu pembukaan popup (bagian 3, halaman dipakai berulang); TC-GS-NLU-504 melanjutkan popup yang sama.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 16 (mengosongkan Number sisa TC-GS-NLU-503 sebelum TC-GS-NLU-504; S-09), langkah 23 (Search untuk menemukan baris target; R-16), langkah 25 (membuka Detail).
- Temuan untuk QA:
  - TC-GS-NLU-504 tidak menyebut cara menemukan baris yang baru dibuat; spec mencari lewat Name bersuffix di langkah 23 (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
  - TC-GS-NLU-503 langkah 4 menyebut "Hapus satu digit terakhir" tanpa menulis nilai hasilnya; spec menulis `123456789012345` dari kolom Data Uji.
  - TC-GS-NLU-504 Expected b ("Submit sukses") tidak menyebut toast; spec mengasersi toast `Success, non-login user has been created.` sama seperti TC Create lain.
  - TC-GS-NLU-502 Expected b ("kode panggilan negara dari katalog") tidak menyebut isi katalog atau jumlah opsi; spec mengasersi keberadaan opsi dan ketiadaan opsi kosong saja.

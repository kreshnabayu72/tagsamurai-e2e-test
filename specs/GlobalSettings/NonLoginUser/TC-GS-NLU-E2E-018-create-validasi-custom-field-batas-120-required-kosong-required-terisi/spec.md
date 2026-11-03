---
id: TC-GS-NLU-E2E-018-create-validasi-custom-field-batas-120-required-kosong-required-terisi
title: "Create: validasi Custom Field (batas 120, Required kosong, Required terisi)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-95
  - TC-GS-NLU-456
  - TC-GS-NLU-457
coverage:
  web: automated
---

# Create: validasi Custom Field (batas 120, Required kosong, Required terisi)

## Prerequisites

- Mode: FE+BE (backend nyata; Custom Field dan record dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By), Custom Field `Badge Note` (Text, Active, tidak Required; dipakai TC-GS-NLU-95 tanpa diubah).
- Custom Field uji `Badge Required` (Text), milik spec: dibuat dan diaktifkan dengan Required Field `On` oleh hook `before` (lewat API; mekanisme disediakan tim FE/BE; Global Settings > Custom Field User > Edit > Required Field `On`), dan dinonaktifkan atau dihapus di hook `after` (dikembalikan menjadi non-Required sebelum dihapus; Post Condition TC-GS-NLU-456 dan TC-GS-NLU-457). Tiga Custom Field dasar tidak diubah.
- Data Dinamis: First Name `Hadi`. TC-GS-NLU-456 memakai Last Name `Kurnia Satu {runId}-018` dan Email `hadikurnia+{runId}-018@qwertysystem.net` (tidak tersimpan); TC-GS-NLU-457 memakai Last Name `Kurnia Dua {runId}-018` dan Email `hadikurnia2+{runId}-018@qwertysystem.net` dan Badge Required `Kartu A` (tersimpan). Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-018` lewat API.
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: Custom Field `Badge Required` (Required Field `On`), dipulihkan di hook `after`. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-95: Custom Field Text lebih dari 120 karakter

1. Klik `[+ Non-Login User]`
2. Isi Badge Note dengan 121 karakter `a`
3. Verifikasi pesan inline `Max. 120 characters` di bawah Badge Note
4. Klik `[Clear Field]`

### TC-GS-NLU-456: Custom Field Required yang dikosongkan ditolak

5. Isi First Name `Hadi`, Last Name `Kurnia Satu {runId}-018`, Email `hadikurnia+{runId}-018@qwertysystem.net`, pilih Division `Logistics` dan Represented By `Ahmad Fauzi`, biarkan `Badge Required` kosong
6. Klik `[Submit]`
7. Verifikasi pesan inline `Badge required must not be empty` di bawah field Badge Required
8. Verifikasi Popup Create tetap terbuka
9. Verifikasi field First Name, Last Name, Email, Division, dan Represented By yang valid tetap terisi

### TC-GS-NLU-457: Custom Field Required yang diisi diterima

10. Ubah Last Name menjadi `Kurnia Dua {runId}-018` dan Email menjadi `hadikurnia2+{runId}-018@qwertysystem.net`
11. Isi `Badge Required` dengan `Kartu A`
12. Verifikasi tidak ada pesan inline pada Badge Required
13. Klik `[Submit]`
14. Verifikasi tersimpan sukses
15. Ketik Search `Hadi Kurnia Dua {runId}-018`, tekan Enter
16. Verifikasi Non-Login User `Hadi Kurnia Dua {runId}-018` tampil di list
17. Buka Detail `Hadi Kurnia Dua {runId}-018` dan perluas bagian Custom Fields
18. Verifikasi Detail menampilkan Badge Required `Kartu A`

### TC-GS-NLU-456 (lanjutan): tidak ada Non-Login User baru dari Submit yang ditolak

19. Kembali ke User List sub-tab Non-Login User, ketik Search `Hadi Kurnia Satu {runId}-018`, tekan Enter
20. Verifikasi tabel menampilkan empty state `No results found`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Validasi diblokir (TC-GS-NLU-95, TC-GS-NLU-456) mendahului aksi sukses (TC-GS-NLU-457; S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 (`[Clear Field]` agar Badge Note 121 karakter tidak terbawa), langkah 10 (Last Name dan Email diganti supaya record TC-GS-NLU-457 dapat dibedakan dari nama TC-GS-NLU-456 yang tidak tersimpan), langkah 15 dan 19 (Search untuk menemukan baris target; R-16), langkah 17 (membuka Detail).
- Klausa "tidak ada Non-Login User baru di list" pada Expected b TC-GS-NLU-456 tidak dapat diamati dari tabel selama Popup terbuka; klausa itu diasersi di langkah 20 sesudah TC-GS-NLU-457, memakai Name TC-GS-NLU-456 (`Hadi Kurnia Satu {runId}-018`) yang tidak tersimpan. Empty state `No results found` hasil Search menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition TC-GS-NLU-456 dan TC-GS-NLU-457 ("Badge Required dikembalikan menjadi non-Required") tidak punya langkah observasi di TC sehingga tidak diasersi; pemulihan dilakukan hook `after`.
  - TC-GS-NLU-456 dan TC-GS-NLU-457 tidak menyebut cara menemukan baris; spec mencari lewat Name bersuffix di langkah 15 dan 19 (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
  - TC-GS-NLU-95 memakai Custom Field Pre-setup `Badge Note` yang tidak diubah; TC-GS-NLU-456 dan TC-GS-NLU-457 memakai `Badge Required` yang diubah menjadi Required sehingga spec menyiapkannya sendiri di hook `before`.

---
id: TC-GS-NLU-E2E-130-popup-select-user-sort-tiga-tahap-per-kolom
title: "Popup Select User: Sort tiga tahap per kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-118
coverage:
  web: automated
---

# Popup Select User: Sort tiga tahap per kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 dengan sedikitnya dua nilai distinct pada kolom Email, Position, Division, dan Name, serta sedikitnya satu baris tanpa Position (Fajar Nugroho). Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- Kolom yang diuji pada langkah 3 sampai 8: Email, Division, Status, Name. Kolom Position diuji pada langkah 9 sampai 14.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-118: Sort 3 tahap pada kolom teks Popup Select User

Untuk setiap kolom pada daftar (Email, Division, Status, Name), lakukan langkah 3 sampai 8.

3. Klik header kolom satu kali
4. Verifikasi baris terurut ascending (A-Z) pada kolom tersebut
5. Klik header kolom satu kali lagi
6. Verifikasi baris terurut descending (Z-A) pada kolom tersebut
7. Klik header kolom satu kali lagi
8. Verifikasi urutan kembali ke default sort Name A-Z
9. Klik header Position satu kali
10. Verifikasi baris terurut ascending (A-Z) pada kolom Position dan baris dengan Position kosong berada di akhir
11. Klik header Position satu kali lagi
12. Verifikasi baris terurut descending (Z-A) pada kolom Position dan baris dengan Position kosong berada di awal
13. Klik header Position satu kali lagi
14. Verifikasi urutan kembali ke default sort Name A-Z
15. Klik `[Cancel]`
16. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 3 sampai 8 diulang untuk empat kolom (Email, Division, Status, Name) dan langkah 9 sampai 14 untuk Position sehingga ekspansi 2 + 4 x 6 + 6 + 2 = 34 langkah, di bawah batas sekitar 35. Position dipisah dari ulangan karena memuat `Verifikasi` tambahan tentang baris dengan Position kosong.
- Langkah penghubung tanpa `Verifikasi`: langkah 15 sampai 16 (menutup popup; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes).
- Temuan untuk QA:
  - Pool Login User pada Popup Select User hanya berstatus Active (TC-GS-NLU-103), sehingga kolom Status hanya memiliki satu nilai distinct dan urutan ascending dan descending kolom Status tidak dapat dibedakan (S-11, S-14). Spec tetap mengikuti TC.
  - TC-GS-NLU-118 langkah 4 ("Ulangi untuk ... Name") tidak menjelaskan hasil klik pertama pada Name, karena Name sudah menjadi default sort A-Z; spec menulis ascending, descending, lalu default sama seperti kolom lain.

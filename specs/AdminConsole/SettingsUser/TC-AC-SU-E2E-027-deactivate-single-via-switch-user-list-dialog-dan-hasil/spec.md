---
id: TC-AC-SU-E2E-027-deactivate-single-via-switch-user-list-dialog-dan-hasil
title: "Deactivate Single via Switch User List: Dialog Konfirmasi, Cancel, Penutupan, dan Hasil Confirm"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-81
  - TC-AC-SU-82
  - TC-AC-SU-83
  - TC-AC-SU-84
  - TC-AC-SU-85
  - TC-AC-SU-86
coverage:
  web: automated
---

# Deactivate Single via Switch User List: Dialog Konfirmasi, Cancel, Penutupan, dan Hasil Confirm

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Jam server dan jam browser sinkron (asersi Last Updated = waktu aksi, toleransi satu menit; bagian 10 S-12).
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-81 s.d. 86 | `Region A` | `Region A {runId}-027` | - | Group |
| TC-AC-SU-81 s.d. 86 | `John Doe` | `John Doe {runId}-027` | `johndoe+{runId}-027@qwertysystem.net` | Activated (sudah aktivasi), Active, tanpa sesi aktif; Global Role `Manage group` ON dan Group Role `Manage allocation` di `Region A {runId}-027` |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-81: Screening dialog Deactivate User dari switch Active di User List

1. Ketik Search `John Doe {runId}-027`, tekan Enter
2. Klik switch Active baris `John Doe {runId}-027`
3. Verifikasi dialog konfirmasi muncul: Title `Deactivate User` dengan icon `[×]`; Body bullet `John Doe {runId}-027`, `This user will lose portal access.`, `Are you sure you want to deactivate it?`; tombol `[Cancel]` (Text, Contrast) dan `[Deactivate]` (filled, danger)
4. Verifikasi dialog `severity="danger"`
5. Verifikasi bullet berisi `John Doe {runId}-027`
6. Klik `[Cancel]` pada dialog

### TC-AC-SU-83: Deactivate user via switch, Cancel

7. Klik switch Active baris `John Doe {runId}-027`
8. Klik `[Cancel]` pada dialog Deactivate User
9. Verifikasi dialog tertutup
10. Verifikasi switch kembali ON
11. Verifikasi tidak ada toast

### TC-AC-SU-84: Deactivate user via switch, tutup dialog lewat icon [×]

12. Klik switch Active baris `John Doe {runId}-027`
13. Klik icon `[×]` pada dialog Deactivate User
14. Verifikasi dialog tertutup
15. Verifikasi switch tetap ON
16. Verifikasi tidak ada toast

### TC-AC-SU-85: Deactivate user via switch, tekan Esc pada dialog

17. Klik switch Active baris `John Doe {runId}-027`
18. Tekan `Esc`
19. Verifikasi dialog tertutup (setara `[×]`)
20. Verifikasi switch tetap ON
21. Verifikasi tidak ada toast

### TC-AC-SU-86: Dialog Deactivate, klik backdrop tidak menutup dialog

22. Klik switch Active baris `John Doe {runId}-027`
23. Klik area di luar dialog (backdrop)
24. Verifikasi dialog tetap terbuka
25. Verifikasi switch belum berubah
26. Klik `[Cancel]` pada dialog Deactivate User

### TC-AC-SU-82: Deactivate user via switch User List, Confirm

27. Klik switch Active baris `John Doe {runId}-027`
28. Klik `[Deactivate]` pada dialog Deactivate User
29. Verifikasi dialog tertutup
30. Verifikasi toast sukses: "Success, user has been deactivated."
31. Verifikasi switch baris `John Doe {runId}-027` OFF
32. Verifikasi Modified By baris `John Doe {runId}-027` = nama singkat akun aktor Total Control (`[First Name] [Last Initial]`)
33. Verifikasi Last Updated baris `John Doe {runId}-027` = waktu aksi (toleransi satu menit)
34. Muat ulang halaman dengan F5
35. Ketik Search `John Doe {runId}-027`, tekan Enter
36. Verifikasi status `John Doe {runId}-027` Inactive (switch OFF) tetap setelah refresh
37. Klik Name `John Doe {runId}-027`
38. Klik Tab Role
39. Verifikasi Global Role `Manage group` pada Detail tetap aktif (ON) seperti sebelum aksi
40. Klik sub-tab Group Role
41. Verifikasi Group Role `Manage allocation` pada Detail tetap tampil dengan group `Region A {runId}-027` seperti sebelum aksi
42. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
43. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk Search sesudahnya), langkah 6 dan 26 (tutup dialog sebelum TC berikutnya, S-09), langkah 34 (muat ulang untuk Post Condition TC-AC-SU-82), langkah 42 dan 43 (kembali ke daftar dan reset Search).
- Urutan TC dalam spec (S-10): 81, 83, 84, 85, 86, lalu 82 (Confirm mengubah status, di akhir). Dialog TC-AC-SU-81 dibuka lalu ditutup dengan `[Cancel]` sebelum TC-AC-SU-83 memulai dari keadaan bersih.
- Ukuran spec (43 langkah, di atas smell sekitar 35 langkah): satu dialog (Deactivate User), satu user, satu halaman; enam blok TC berdiri sendiri (tiap blok dimulai dari switch ON dan dialog tertutup, S-09), dan blok TC-AC-SU-82 memuat dua observasi Post Condition yang diberikan TC (refresh dan Tab Role).
- Temuan untuk QA:
  - TC-AC-SU-82 butir d: "nama singkat aktor" tidak menyebut nama aktor; nama tampil akun aktor Pre-setup #2 tidak tertulis di Pre-setup. Spec mengasersi format `[First Name] [Last Initial]` (R-14) dari akun aktor.
  - TC-AC-SU-82 Post Condition c ("Log Deactivate tercatat ... diverifikasi di Section 5") tidak punya langkah observasi di TC ini dan tidak diasersi (S-01); TC-AC-SU-83 sampai 85 Post Condition "tidak ada entri log baru" juga tidak diasersi.
  - TC-AC-SU-81 Post Condition "Status belum berubah (Active)" tidak punya langkah observasi di TC; keadaan switch tetap ON diasersi di TC-AC-SU-83.
  - Nama user TC (`John Doe`, `Region A`) dipakai sebagai nama bersuffix `{runId}-027` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).

---
id: TC-GS-NLU-E2E-020-create-validasi-employee-id-duplikat-beda-huruf-besar-kecil-karakter-khusus
title: "Create: validasi Employee ID duplikat, beda huruf besar kecil, dan karakter khusus"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-72
  - TC-GS-NLU-73
  - TC-GS-NLU-74
  - TC-GS-NLU-461
coverage:
  web: automated
---

# Create: validasi Employee ID duplikat, beda huruf besar kecil, dan karakter khusus

## Prerequisites

- Mode: FE+BE (backend nyata; duplikasi Employee ID divalidasi server).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Login User `Ahmad Fauzi` (Employee ID `EMP-0001`, No. 10), Division `Logistics`.
- Data Dinamis milik spec, semua Employee ID bersuffix `{runId}-020`:
  - Seed hook `before` lewat API (mekanisme disediakan tim FE/BE): Non-Login User `Seed Duplikat {runId}-020` (First Name `Seed`, Last Name `Duplikat {runId}-020`, Employee ID `AB-{runId}-020`, Email `seedduplikat+{runId}-020@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`), dipakai TC-GS-NLU-73 (duplikat `AB-{runId}-020`) dan TC-GS-NLU-74 (varian huruf kecil `ab-{runId}-020`).
  - TC-GS-NLU-74 (tersimpan dengan Employee ID `ab-{runId}-020`): First Name `Kecil`, Last Name `Huruf`, Email `kecilhuruf+{runId}-020@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`.
  - TC-GS-NLU-461 (tersimpan dengan Employee ID `EMP/2026-001 #A-{runId}-020`): First Name `Karakter`, Last Name `Khusus {runId}-020`, Email `karakterkhusus+{runId}-020@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-020` (termasuk seed) lewat API (mekanisme disediakan tim FE/BE).
- Kemampuan teknis: menunggu sekitar 500 ms sesudah mengetik Employee ID (jeda pendek yang disebut TC).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-72: Employee ID sudah dipakai Login User

1. Klik `[+ Non-Login User]`
2. Ketik Employee ID `EMP-0001`, lalu tunggu sekitar 500 ms
3. Verifikasi pesan inline `Employee ID already exists`
4. Klik `[Clear Field]`

### TC-GS-NLU-73: Employee ID sudah dipakai Non-Login User lain

5. Ketik Employee ID `AB-{runId}-020`, lalu tunggu sekitar 500 ms
6. Verifikasi pesan inline `Employee ID already exists`
7. Klik `[Clear Field]`

### TC-GS-NLU-74: Employee ID yang hanya beda huruf besar kecil dianggap berbeda

8. Ketik Employee ID `ab-{runId}-020`, lalu tunggu sekitar 500 ms
9. Verifikasi field Employee ID berisi `ab-{runId}-020`
10. Verifikasi tidak ada pesan `Employee ID already exists` (pembanding case-sensitive)
11. Lengkapi field wajib lain: First Name `Kecil`, Last Name `Huruf`, Email `kecilhuruf+{runId}-020@qwertysystem.net`, pilih Division `Logistics` dan Represented By `Ahmad Fauzi`
12. Klik `[Submit]`
13. Verifikasi data tersimpan sukses dengan toast `Success, non-login user has been created.`

### TC-GS-NLU-461: Employee ID dengan karakter khusus diterima tanpa helper text

14. Klik `[+ Non-Login User]`
15. Isi First Name `Karakter` dan Last Name `Khusus {runId}-020`
16. Pilih Division `Logistics` dan isi Email `karakterkhusus+{runId}-020@qwertysystem.net`
17. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
18. Isi Employee ID `EMP/2026-001 #A-{runId}-020`
19. Verifikasi tidak ada pesan error karakter pada Employee ID
20. Verifikasi tidak ada helper text di bawah field Employee ID
21. Klik `[Submit]`
22. Verifikasi create sukses dengan toast `Success, non-login user has been created.`
23. Ketik Search `Karakter Khusus {runId}-020`, tekan Enter
24. Buka Detail record `Karakter Khusus {runId}-020`
25. Verifikasi Detail menampilkan Employee ID `EMP/2026-001 #A-{runId}-020`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Validasi diblokir (TC-GS-NLU-72, 73) mendahului aksi sukses (TC-GS-NLU-74, 461; S-10).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4 dan 7 (`[Clear Field]` karena pesan inline identik berurutan pada form yang sama; R-12), langkah 23 (Search untuk menemukan baris target; R-16), langkah 24 (membuka Detail).
- Langkah 9 adalah anchor positif untuk asersi absence langkah 10 (bagian 8b butir 2): field Employee ID terisi `ab-{runId}-020` sesudah jeda 500 ms.
- Langkah 11 memakai Email dan nilai field wajib lain pilihan spec karena TC-GS-NLU-74 hanya menulis "Lengkapi field wajib lain".
- Temuan untuk QA:
  - TC-GS-NLU-73 dan TC-GS-NLU-74 memakai Employee ID Pre-setup `FT-0231` dan varian `ft-0231` yang disimpan literal; nilai tersimpan itu bentrok antar run. Spec memakai record seed milik spec dengan Employee ID `AB-{runId}-020` dan varian `ab-{runId}-020`; TC-GS-NLU-461 menyimpan `EMP/2026-001 #A-{runId}-020` (suffix `{runId}` ditambah di akhir nilai; S-12). Perbedaan huruf besar kecil dan karakter khusus tetap diuji.
  - TC-GS-NLU-74 Expected b ("Data tersimpan sukses") dan TC-GS-NLU-461 Expected b menyebut toast `Success, non-login user has been created.` hanya pada TC-GS-NLU-461; untuk TC-GS-NLU-74 spec memakai teks toast yang sama dengan TC-GS-NLU-461.
  - TC-GS-NLU-461 langkah 9 (buka Detail record tersebut) tidak menyebut cara menemukan baris; spec mencari lewat Name bersuffix di langkah 23 (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).

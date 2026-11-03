---
id: TC-GS-NLU-E2E-049-edit-referensi-represented-by-position-division-custom-field-dihapus
title: "Edit: referensi Represented By, Position, Division, Custom Field dihapus atau di-rename sebelum Save"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-160
  - TC-GS-NLU-161
  - TC-GS-NLU-163
  - TC-GS-NLU-164
  - TC-GS-NLU-165
coverage:
  web: automated
---

# Edit: referensi Represented By, Position, Division, Custom Field dihapus atau di-rename sebelum Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json`, nilai dirujuk sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Sesi API aktor: pelaku kedua yang menghapus dan me-rename entitas memakai sesi API akun Total Control yang sama dengan sesi UI, sesuai pernyataan Sesi API aktor di `suite.md`.
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Division `Operations` dan pool Login User Represented By `Ahmad Fauzi`. Tidak ada data Pre-setup yang dihapus atau di-rename.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after` bila masih ada; mekanisme seeding dan penghapusan disediakan tim FE/BE): Non-Login User target Edit Target 19 (First Name `Edit Target 19`, Last Name `{runId}-049`, Email `edittarget19+{runId}-049@qwertysystem.net`, Division `Operations`, Represented By `Ahmad Fauzi`, Active); Login User `Wakil Hapus Uji {runId}-049` (Active, TC-GS-NLU-160) dan `Wakil Rename {runId}-049` (Active, TC-GS-NLU-161); Position `Posisi Hapus {runId}-049` (TC-GS-NLU-163) dan `Posisi Rename {runId}-049` (TC-GS-NLU-161); Division `Divisi Hapus {runId}-049` (TC-GS-NLU-164) dan `Divisi Rename {runId}-049` (TC-GS-NLU-161); Custom Field uji `Blood Type Uji` (Dropdown dengan opsi A, B, O, AB, aktif, dibuat hook `before` dan dihapus hook `after`; TC-GS-NLU-165). Pada TC-GS-NLU-161, nama baru hasil rename adalah `Wakil Rename Baru {runId}-049`, `Posisi Rename Baru {runId}-049`, dan `Divisi Rename Baru {runId}-049`.
- Data uji tidak memakai `Wawan Setiadi`, `Driver`, `Logistics`, dan `Ahmad Fauzi` yang disebut TC sebagai entitas yang dihapus atau di-rename, karena itu data Pre-setup bersama (S-06); spec memakai entitas milik spec.
- State global: tidak ada yang diubah selain entitas milik spec di atas.

## Test Steps

1. Ketik Search `Edit Target 19 {runId}-049`, tekan Enter
2. Klik `⋯` pada baris Edit Target 19 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-160: Represented By yang dihapus atau dinonaktifkan sebelum submit ditolak server pada Popup Edit

3. Pilih Represented By `Wakil Hapus Uji {runId}-049` lewat Popup Select User
4. Hapus Login User `Wakil Hapus Uji {runId}-049` lewat sesi API aktor hingga terhapus
5. Klik `[Save]`
6. Verifikasi pesan inline di bawah Represented By `This user no longer exists. Please select another.`
7. Verifikasi Represented By kembali ke `[+ Select User]` (badge hilang)
8. Verifikasi field lain yang valid tetap terisi
9. Verifikasi Popup Edit tetap terbuka

### TC-GS-NLU-163: Position yang dihapus sebelum submit ditolak server pada Popup Edit

10. Pilih Represented By `Ahmad Fauzi` lewat Popup Select User
11. Pilih Position `Posisi Hapus {runId}-049`
12. Hapus Position `Posisi Hapus {runId}-049` lewat sesi API aktor hingga terhapus
13. Klik `[Save]`
14. Verifikasi pesan inline di bawah dropdown Position `This position no longer exists. Please select another.`
15. Verifikasi pilihan Position auto-clear
16. Klik dropdown Position
17. Verifikasi opsi Position di-fetch ulang: `Posisi Hapus {runId}-049` tidak ada dan sedikitnya satu opsi Position lain tampil
18. Verifikasi field lain tetap terisi
19. Verifikasi Popup Edit tetap terbuka

### TC-GS-NLU-164: Division yang dihapus sebelum submit ditolak server pada Popup Edit

20. Pilih Division `Divisi Hapus {runId}-049`
21. Hapus Division `Divisi Hapus {runId}-049` lewat sesi API aktor hingga terhapus
22. Klik `[Save]`
23. Verifikasi pesan inline di bawah dropdown Division `This division no longer exists. Please select another.`
24. Verifikasi pilihan Division auto-clear
25. Klik dropdown Division
26. Verifikasi opsi Division di-fetch ulang: `Divisi Hapus {runId}-049` tidak ada dan sedikitnya satu opsi Division lain tampil
27. Verifikasi field lain tetap terisi
28. Verifikasi Popup Edit tetap terbuka

### TC-GS-NLU-165: Custom Field dropdown yang dihapus sebelum submit ditolak server pada Popup Edit

29. Pilih Division `Operations`
30. Pilih Blood Type Uji `AB`
31. Hapus opsi `AB` dari Custom Field Blood Type Uji lewat sesi API aktor hingga terhapus
32. Klik `[Save]`
33. Verifikasi pesan inline di bawah Blood Type Uji `This blood type uji no longer exists. Please select another.`
34. Verifikasi pilihan Blood Type Uji auto-clear
35. Verifikasi field lain tetap terisi
36. Verifikasi Popup Edit tetap terbuka

### TC-GS-NLU-161: Rename Position, Division, atau Represented By sebelum submit bukan error pada Popup Edit

37. Pilih Position `Posisi Rename {runId}-049`, Division `Divisi Rename {runId}-049`, dan Represented By `Wakil Rename {runId}-049`
38. Ubah nama Position, Division, dan Login User menjadi `Posisi Rename Baru {runId}-049`, `Divisi Rename Baru {runId}-049`, dan `Wakil Rename Baru {runId}-049` lewat sesi API aktor hingga tersimpan
39. Klik `[Save]`
40. Verifikasi toast sukses `Success, non-login user has been updated.`
41. Buka Detail record tersebut
42. Verifikasi Detail menampilkan nama terbaru ketiga referensi (Position, Division, dan Represented By)

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini melewati sekitar 35 langkah (nominal 42). Alasan: kelima TC satu topik (referensi dihapus atau di-rename sebelum Save) dan memakai satu pembukaan Popup Edit sesuai prinsip halaman yang sama dipakai berulang; pemecahan menambah login, seeding, dan pembukaan form tanpa pemisah nyata. Tiap blok memilih referensinya sendiri dan menghapus atau me-rename entitas milik spec sendiri lewat sesi API aktor, sehingga kegagalan asersi satu blok tidak mengubah makna blok berikutnya. Kegagalan keras (popup tidak terbuka) menghentikan seluruh blok.
- Urutan: TC-GS-NLU-160, TC-GS-NLU-163, TC-GS-NLU-164, dan TC-GS-NLU-165 (ditolak server, popup tetap terbuka) lebih dulu, TC-GS-NLU-161 (Save sukses) terakhir (S-10).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (Search Name bersuffix untuk menemukan baris target, R-16; Email bukan kolom Search List); langkah 10 dan 29 (memilih kembali Represented By dan Division yang dikosongkan blok sebelumnya supaya validasi required sisi klien tidak menutupi respons server).
- Pelaku kedua memakai sesi API aktor; id `P-2` tidak dipakai (keputusan 2026-10-30).
- Nama Custom Field uji `Blood Type Uji` literal (bukan bersuffix `{runId}`) karena pesan error TC-GS-NLU-165 memuat nama field; ini butir Lampiran A yang masih tertunda untuk modul Non-Login User dan dicatat di sini saja.
- Temuan untuk QA:
  - TC-GS-NLU-160 sampai TC-GS-NLU-165 menyebut tindakan "di sesi lain" tanpa menyebut siapa pelakunya; spec memakai sesi API aktor Total Control.
  - TC-GS-NLU-160 menulis "nonaktifkan atau hapus Wawan Setiadi"; spec memilih menghapus Login User milik spec.
  - TC-GS-NLU-163 dan TC-GS-NLU-164 Expected butir b ("opsi di-fetch ulang") tidak menyebut cara mengamatinya; spec membuka dropdown dan mengasersi opsi yang dihapus tidak ada.
  - TC-GS-NLU-160 Expected butir c ("Field lain yang valid tetap terisi") tidak menyebut field mana; spec mengasersi field lain secara umum tetap terisi.

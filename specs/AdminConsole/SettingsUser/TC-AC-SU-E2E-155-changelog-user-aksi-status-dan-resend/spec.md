---
id: TC-AC-SU-E2E-155-changelog-user-aksi-status-dan-resend
title: "Popup Changelog: User dan Tab Changelog Detail Mencatat Aksi Activate, Deactivate, Resend Activation Email, dan Resend Confirmation Email dari Settings > User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-531
  - TC-AC-SU-532
  - TC-AC-SU-533
  - TC-AC-SU-534
coverage:
  web: automated
---

# Popup Changelog: User dan Tab Changelog Detail Mencatat Aksi Activate, Deactivate, Resend Activation Email, dan Resend Confirmation Email dari Settings > User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec; hook `after` memulihkan sesi ke akun default suite.
- Data Dinamis (di-seed di hook `before` lewat Fixture BE, dihapus di hook `after`; nama dan email bersuffix `{runId}-155`, baseline entri Changelog nol karena nama unik):

| Kode | Name | Email | Status |
|---|---|---|---|
| U1 | `Jane Smith {runId}-155` | `janesmith+{runId}-155@qwertysystem.net` | Activated, Inactive |
| U2 | `John Doe {runId}-155` | `johndoe+{runId}-155@qwertysystem.net` | Activated, Active |
| U3 | `Sarah Lee {runId}-155` | `sarahlee+{runId}-155@qwertysystem.net` | Pending Activation, di luar cooldown Resend |
| U4 | `Rina Putri {runId}-155` | email pending baru `rinaputri+{runId}-155@qwertysystem.net` | Pending Email Confirmation, di luar cooldown Resend |

- Kemampuan teknis: Fixture BE (seeding dan penghapusan user); nama tampil akun aktor Total Control untuk Modified By format `[First Name] [Last Initial]` dibaca dari fixture (`Fixture.settingsUser.totalControlActor.modifiedBy`; nama tampil tidak tertulis di Pre-setup TC, lihat Temuan untuk QA). Jam server dan jam browser sinkron; waktu aksi dicatat sesudah aksi dan Date dibandingkan dengan toleransi satu menit. Tidak memakai intercept atau klien HTTP.
- Format Date mengikuti General Settings yang berlaku (tidak diubah spec ini).
- Suite berjalan serial (`parallel: false`). Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-SU-531: Aksi Activate tercatat

1. Ketik Search `Jane Smith {runId}-155`, tekan Enter
2. Toggle Active OFF ke ON pada baris U1
3. Klik `[Activate]` pada dialog Activate User, lalu catat waktu aksi
4. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
5. Verifikasi baris teratas: Action `Activate`, User Name `Jane Smith {runId}-155`, Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By nama aktor format singkat
6. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
7. Tutup Popup Changelog: User, buka Detail U1 (klik Name pada baris), klik Tab Changelog
8. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Activate`, Field `Status`, Old Value `Inactive`, New Value `Active`)
9. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

### TC-AC-SU-532: Aksi Deactivate tercatat

10. Klik menu Settings > User di sidebar
11. Ketik Search `John Doe {runId}-155`, tekan Enter
12. Toggle Active ON ke OFF pada baris U2
13. Klik `[Deactivate]` pada dialog Deactivate User, lalu catat waktu aksi
14. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
15. Verifikasi baris teratas: Action `Deactivate`, User Name `John Doe {runId}-155`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By nama aktor format singkat
16. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
17. Tutup Popup Changelog: User, buka Detail U2, klik Tab Changelog
18. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Deactivate`, Field `Status`, Old Value `Active`, New Value `Inactive`)
19. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

### TC-AC-SU-533: Aksi Resend Activation Email tercatat

20. Klik menu Settings > User di sidebar
21. Ketik Search `Sarah Lee {runId}-155`, tekan Enter
22. Buka row action (⋯) baris U3, klik Resend Activation Email, lalu catat waktu aksi
23. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka (tutup dan buka ulang tiap 5 detik sampai entri muncul, batas tunggu 30 detik)
24. Verifikasi baris teratas: Action `Resend Activation Email`, User Name `Sarah Lee {runId}-155`, Field `Activation Email`, Old Value `—`, New Value `sarahlee+{runId}-155@qwertysystem.net`, Modified By nama aktor format singkat
25. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
26. Tutup Popup Changelog: User, buka Detail U3, klik Tab Changelog
27. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Resend Activation Email`, Field `Activation Email`, Old Value `—`, New Value `sarahlee+{runId}-155@qwertysystem.net`)
28. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

### TC-AC-SU-534: Aksi Resend Confirmation Email tercatat

29. Klik menu Settings > User di sidebar
30. Ketik Search `Rina Putri {runId}-155`, tekan Enter
31. Buka row action (⋯) baris U4, klik Resend Confirmation Email, lalu catat waktu aksi
32. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka (tutup dan buka ulang tiap 5 detik sampai entri muncul, batas tunggu 30 detik)
33. Verifikasi baris teratas: Action `Resend Confirmation Email`, User Name `Rina Putri {runId}-155`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri+{runId}-155@qwertysystem.net`, Modified By nama aktor format singkat
34. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
35. Tutup Popup Changelog: User, buka Detail U4, klik Tab Changelog
36. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Resend Confirmation Email`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri+{runId}-155@qwertysystem.net`)
37. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): langkah 1, 11, 21, 30 (Search untuk menemukan baris target, R-16), langkah 7, 17, 26, 35 (menutup popup dan membuka Detail), langkah 10, 20, 29 (kembali ke daftar lewat sidebar), pencatatan waktu aksi pada langkah 3, 13, 22, 31.
- Urutan: Expected TC menempatkan Tab Changelog (butir c) sesudah Popup Changelog; spec memverifikasi Popup lebih dulu lalu Tab Changelog mengikuti urutan state layar. Baris target dicari sebagai baris teratas (Newest First) karena aksi baru saja dilakukan (S-14); nama unik per spec membuat baseline nol.
- Spec berisi empat blok TC independen berpola sama (aktor, surface, dan jenis asersi identik; tiap blok memakai user seeding sendiri), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; 37 langkah (di atas smell 35 langkah) dipertahankan karena pola identik itu.
- Temuan untuk QA:
  - Post Condition TC-531 sampai TC-534 (Tab System Log aktor dan Activity Log dicatat) tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan System Log dan Activity Log diasersi pada spec 166 sampai 168.
  - Nama tampil akun Total Control tidak tertulis di Pre-setup TC (TC hanya memberi contoh `Admin U`); nilai Modified By diambil dari fixture yang disediakan tim FE.
  - TC memakai nama literal (`Jane Smith`, `John Doe`, `Sarah Lee`, `Rina Putri`) dan email `sarahlee@qwertysystem.net`; spec memakai nama dan email bersuffix `{runId}-155` sesuai S-12.
  - TC-533 dan TC-534 tidak menyatakan jeda penulisan entri Resend; spec memakai idiom polling 30 detik dari TC-578.

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
4. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
5. Ketik Search `Jane Smith {runId}-155` pada Popup Changelog: User, tekan Enter
6. Verifikasi tepat 1 baris: Action `Activate`, User Name `Jane Smith {runId}-155`, Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By nama aktor format singkat
7. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
8. Tutup Popup Changelog: User, buka Detail U1 (klik Name pada baris), klik Tab Changelog
9. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Activate`, Field `Status`, Old Value `Inactive`, New Value `Active`)
10. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

### TC-AC-SU-532: Aksi Deactivate tercatat

11. Klik menu Settings > User di sidebar
12. Ketik Search `John Doe {runId}-155`, tekan Enter
13. Toggle Active ON ke OFF pada baris U2
14. Klik `[Deactivate]` pada dialog Deactivate User, lalu catat waktu aksi
15. Tunggu aksi selesai, lalu klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
16. Ketik Search `John Doe {runId}-155` pada Popup Changelog: User, tekan Enter
17. Verifikasi tepat 1 baris: Action `Deactivate`, User Name `John Doe {runId}-155`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By nama aktor format singkat
18. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
19. Tutup Popup Changelog: User, buka Detail U2, klik Tab Changelog
20. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Deactivate`, Field `Status`, Old Value `Active`, New Value `Inactive`)
21. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

### TC-AC-SU-533: Aksi Resend Activation Email tercatat

22. Klik menu Settings > User di sidebar
23. Ketik Search `Sarah Lee {runId}-155`, tekan Enter
24. Buka row action (⋯) baris U3, klik Resend Activation Email, lalu catat waktu aksi
25. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
26. Ketik Search `Sarah Lee {runId}-155` pada Popup Changelog: User, tekan Enter (tutup dan buka ulang popup lalu Search ulang tiap 5 detik sampai entri muncul, batas tunggu 30 detik)
27. Verifikasi tepat 1 baris: Action `Resend Activation Email`, User Name `Sarah Lee {runId}-155`, Field `Activation Email`, Old Value `—`, New Value `sarahlee+{runId}-155@qwertysystem.net`, Modified By nama aktor format singkat
28. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
29. Tutup Popup Changelog: User, buka Detail U3, klik Tab Changelog
30. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Resend Activation Email`, Field `Activation Email`, Old Value `—`, New Value `sarahlee+{runId}-155@qwertysystem.net`)
31. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

### TC-AC-SU-534: Aksi Resend Confirmation Email tercatat

32. Klik menu Settings > User di sidebar
33. Ketik Search `Rina Putri {runId}-155`, tekan Enter
34. Buka row action (⋯) baris U4, klik Resend Confirmation Email, lalu catat waktu aksi
35. Klik icon Changelog di toolbar sehingga Popup Changelog: User terbuka
36. Ketik Search `Rina Putri {runId}-155` pada Popup Changelog: User, tekan Enter (tutup dan buka ulang popup lalu Search ulang tiap 5 detik sampai entri muncul, batas tunggu 30 detik)
37. Verifikasi tepat 1 baris: Action `Resend Confirmation Email`, User Name `Rina Putri {runId}-155`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri+{runId}-155@qwertysystem.net`, Modified By nama aktor format singkat
38. Verifikasi Date baris sama dengan waktu aksi (toleransi satu menit) dan berformat mengikuti General Settings
39. Tutup Popup Changelog: User, buka Detail U4, klik Tab Changelog
40. Verifikasi Tab Changelog menampilkan entri yang sama (Action `Resend Confirmation Email`, Field `Confirmation Email`, Old Value `—`, New Value `rinaputri+{runId}-155@qwertysystem.net`)
41. Verifikasi tabel Tab Changelog tidak memiliki kolom User Name

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): langkah 1, 12, 23, 33 (Search untuk menemukan baris target, R-16), langkah 5, 16, 26, 36 (Search nama unik pada Popup Changelog: User), langkah 8, 19, 29, 39 (menutup popup dan membuka Detail), langkah 11, 22, 32 (kembali ke daftar lewat sidebar), pencatatan waktu aksi pada langkah 3, 14, 24, 34.
- Urutan: Expected TC menempatkan Tab Changelog (butir c) sesudah Popup Changelog; spec memverifikasi Popup lebih dulu lalu Tab Changelog mengikuti urutan state layar. Entri dicari dengan Search nama bersuffix `{runId}-155` pada Popup Changelog: User; user bernama unik sehingga baseline entri nol dan "tepat 1 baris" menjadi asersi jumlah pada hasil Search, bukan pembacaan baris teratas (S-14).
- Spec berisi empat blok TC independen berpola sama (aktor, surface, dan jenis asersi identik; tiap blok memakai user seeding sendiri), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; 41 langkah (di atas smell 35 langkah) dipertahankan karena pola identik itu.
- Temuan untuk QA:
  - Post Condition TC-531 sampai TC-534 (Tab System Log aktor dan Activity Log dicatat) tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan System Log dan Activity Log diasersi pada spec 166 sampai 168.
  - Nama tampil akun Total Control tidak tertulis di Pre-setup TC (TC hanya memberi contoh `Admin U`); nilai Modified By diambil dari fixture yang disediakan tim FE.
  - TC memakai nama literal (`Jane Smith`, `John Doe`, `Sarah Lee`, `Rina Putri`) dan email `sarahlee@qwertysystem.net`; spec memakai nama dan email bersuffix `{runId}-155` sesuai S-12.
  - TC-533 dan TC-534 tidak menyatakan jeda penulisan entri Resend; spec memakai idiom polling 30 detik dari TC-578.

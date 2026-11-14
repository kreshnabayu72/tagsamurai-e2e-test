---
id: TC-FA-FATR-UI-067-area-respons
title: "Area utama: loading, gagal muat, dan reaksi atas respons Save"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - §7#r1
  - §7#r2
  - §7#r8
  - S-01
  - S-02
  - §9.2#b58
  - §9.2#b59
  - §9.4.2#r24
  - §9.4.2#r65
  - §9.4.2#r85
  - §9.4.2#r86
  - §9.4.2#r94
  - §9.4.2#r95
  - §9.4.2#r96
  - §9.4.4#r15
  - §9.6#r14
  - §9.6#r15
  - EB-FB-1@save-changes
  - EB-FB-3@save-changes
  - EB-FB-4
  - EB-ERR-1@save-changes
smoke: []
dependsOn: []
trace:
  §7#r1: [12, 27]
  §7#r2: [18, 24]
  §7#r8: 42
  S-01: [2, 7, 73]
  S-02: [4, 5, 7]
  §9.2#b58: 18
  §9.2#b59: [24, 35]
  §9.4.2#r24: [64, 65]
  §9.4.2#r65: [70, 71]
  §9.4.2#r85: [49, 55]
  §9.4.2#r86: [50, 56]
  §9.4.2#r94: 18
  §9.4.2#r95: [24, 35]
  §9.4.2#r96: 37
  §9.4.4#r15: 37
  §9.6#r14: 18
  §9.6#r15: [24, 35]
  EB-FB-1@save-changes: [12, 18]
  EB-FB-3@save-changes: [42, 43, 44]
  EB-FB-4: [13, 20, 21, 23]
  EB-ERR-1@save-changes: [25, 27, 32, 33, 34]
anchor: []
coverage:
  web: automated
---

# Area utama: loading, gagal muat, dan reaksi atas respons Save

## Prerequisites
- Aktor: Total Control.
- Layar awal: Area utama pada halaman Transaction Settings.
- Komponen: Area utama
- Data:
  - DU-067-1: Pengaturan Company default tab Borrow pada All categories: Max duration `14`.
  - DU-067-2: Nilai Max duration draft yang dicoba: `10`.
  - DU-067-3: Pengaturan Company default tab Borrow pada All categories yang sudah tersimpan di server dengan Max duration `10`, sementara Area utama masih menampilkan `14`.
  - DU-067-4: Override yang dicoba pada Add override - Borrow: Scope `Group`, Target Group `Head Office`, Field `Allow Borrow`, Value `Deny`.
  - DU-067-5: Pengaturan Company default tab Assign pada All categories: Allow Assign `Allow`, Allowed assignee: Employee `ON`, Allowed assignee: Division `ON`.
- Kondisi:
  - K1: Area utama sedang memuat data halaman dan respons pemuatan belum diterima.
  - K2: Pemuatan data halaman gagal.
  - K3: node All categories terpilih, tab Borrow aktif, nilai memakai DU-067-1, server menjawab Save dengan sukses.
  - K4: node All categories terpilih, tab Borrow aktif, nilai memakai DU-067-1, server menjawab Save dengan kegagalan server (5xx) pada percobaan pertama dan sukses pada percobaan kedua.
  - K5: node All categories terpilih, tab Borrow aktif, nilai memakai DU-067-1, Save tidak mendapat respons sampai timeout.
  - K6: node All categories terpilih, tab Borrow aktif, Area utama memakai DU-067-1 sedangkan server memakai DU-067-3, sehingga Save tiba tanpa selisih.
  - K7: entitas berstatus Suspended, node All categories terpilih, tab Borrow aktif, nilai memakai DU-067-1.
  - K8: entitas berstatus Expired, node All categories terpilih, tab Borrow aktif, nilai memakai DU-067-1.
  - K9: entitas berstatus Suspended, node All categories terpilih, tab Borrow aktif, nilai memakai DU-067-1, dialog Add override diisi dengan DU-067-4.
  - K10: node All categories terpilih, tab Assign aktif, nilai memakai DU-067-5, server menolak Save karena kombinasi efektif Allowed assignee OFF/OFF pada sebuah override yang sudah ada.
  - K11: node All categories terpilih, tab Borrow aktif, nilai memakai DU-067-1, respons daftar override belum diterima.

## Test Steps

### Loading saat data halaman diambil
1. Tampilkan Area utama dengan kondisi K1
2. Verifikasi keadaan loading tampil pada Area utama selama data belum diterima

### Gagal memuat data halaman
3. Tampilkan Area utama dengan kondisi K2
4. Verifikasi pesan `Unable to load this data.` tampil pada Area utama
5. Verifikasi tombol `Try Again` tampil dan aktif
6. Klik `Try Again` dengan respons pemuatan ditahan
7. Verifikasi keadaan loading tampil kembali selama pemuatan ulang berjalan

### Save berhasil
8. Tampilkan Area utama dengan kondisi K3
9. Ubah `Max duration` menjadi `10`
10. Klik `Save`
11. Klik `Save` pada dialog `Save Changes`
12. Verifikasi toast `Success, settings have been saved.` tampil dengan severity success
13. Verifikasi toast sukses itu menutup sendiri setelah 4 detik tanpa tindakan pengguna

### Save gagal karena kegagalan server
14. Tampilkan Area utama dengan kondisi K4
15. Ubah `Max duration` menjadi `10`
16. Klik `Save`
17. Klik `Save` pada dialog `Save Changes`
18. Verifikasi toast `Error, failed to save settings.` tampil
19. Tunggu 4 detik
20. Verifikasi toast gagal itu masih tampil walau 4 detik sudah lewat
21. Verifikasi tombol `Close Button` tampil pada toast gagal
22. Klik tombol `Close Button` pada toast gagal
23. Verifikasi toast gagal itu menutup karena tombol `Close Button` diklik
24. Verifikasi `Max duration` pada draft tetap `10`
25. Verifikasi dialog `Save Changes` tetap terbuka dan tombol `Save` di dalamnya aktif lagi
26. Klik `Save` pada dialog `Save Changes` setelah server pulih
27. Verifikasi toast `Success, settings have been saved.` tampil satu kali

### Save tanpa respons sampai timeout
28. Tampilkan Area utama dengan kondisi K5
29. Ubah `Max duration` menjadi `10`
30. Klik `Save`
31. Klik `Save` pada dialog `Save Changes`
32. Verifikasi toast `Connection problem. Please try again.` tampil[^drift-1]
33. Verifikasi toast itu hanya memuat tombol `Close Button` dan tidak memuat tombol aksi lain
34. Verifikasi dialog `Save Changes` tetap terbuka dan tombol `Save` di dalamnya aktif lagi
35. Verifikasi `Max duration` pada draft tetap `10`
36. Klik `Cancel` pada dialog `Save Changes`
37. Verifikasi tombol `Save` pada Area utama tetap aktif karena draft belum tersimpan

### Save tiba tanpa selisih
38. Tampilkan Area utama dengan kondisi K6
39. Ubah `Max duration` menjadi `10`
40. Klik `Save`
41. Klik `Save` pada dialog `Save Changes`
42. Verifikasi toast `No changes to save.` tampil dengan severity info
43. Verifikasi dialog `Save Changes` sudah tertutup
44. Verifikasi toast `Success, settings have been saved.` tidak ada

### Save ditolak karena entitas Suspended
45. Tampilkan Area utama dengan kondisi K7
46. Ubah `Max duration` menjadi `10`
47. Klik `Save`
48. Klik `Save` pada dialog `Save Changes`
49. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
50. Verifikasi `Max duration` pada draft tetap `10`

### Save ditolak karena entitas Expired
51. Tampilkan Area utama dengan kondisi K8
52. Ubah `Max duration` menjadi `10`
53. Klik `Save`
54. Klik `Save` pada dialog `Save Changes`
55. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
56. Verifikasi draft `Max duration` tidak berubah dari `10` setelah penolakan

### Add override ditolak karena entitas Suspended
57. Tampilkan Area utama dengan kondisi K9
58. Klik `+ Override`
59. Pilih Scope `Group`
60. Pilih Target Group `Head Office` melalui tombol `Select Group`
61. Pilih Field `Allow Borrow`
62. Pilih Value `Deny`
63. Klik `Submit`
64. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
65. Verifikasi dialog `Add override - Borrow` tetap terbuka

### Save ditolak karena Allowed assignee OFF/OFF
66. Tampilkan Area utama dengan kondisi K10
67. Matikan `Allowed assignee: Division`
68. Klik `Save`
69. Klik `Save` pada dialog `Save Changes`
70. Verifikasi `Allowed assignee: Employee` memuat penolakan server `At least one assignee type must be enabled` tepat di bawah kontrolnya
71. Verifikasi `Allowed assignee: Division` memuat penolakan server `At least one assignee type must be enabled` tepat di bawah kontrolnya

### Loading saat daftar override diambil
72. Tampilkan Area utama dengan kondisi K11
73. Verifikasi keadaan loading tampil pada tabel `Overrides` selama daftar override belum diterima

[^drift-1]: Drift PRD vs foundation. PRD §9.4.2 #r94 (EC-11a) dan §9.6 #r14 (RES-SAVE-i): Save Changes 5xx atau timeout memunculkan Toast T-02 `Error, failed to save settings.`. Foundation `error-handling-convention.md` §2 baris Timeout / Network: toast `Connection problem. Please try again.`. Diasersi: foundation, karena copy toast untuk timeout atau jaringan adalah pola bersama platform (SB-4); toast T-02 diasersi pada langkah kegagalan server.

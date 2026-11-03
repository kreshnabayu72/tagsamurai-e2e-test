---
id: TC-AC-ACC-E2E-172-header-detail-badge-tab-dan-client-derived
title: "Header Detail Client: Tab, Sub-tab Awal, Client Derived, Badge Status, dan Badge Default User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-234
  - TC-AC-ACC-235
  - TC-AC-ACC-236
  - TC-AC-ACC-239
  - TC-AC-ACC-240
coverage:
  web: automated
---

# Header Detail Client: Tab, Sub-tab Awal, Client Derived, Badge Status, dan Badge Default User

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; halaman List Admin Console > Client dibuka hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Data Pre-setup Residen (baca-saja, Tabel A2): "PT Sejahtera Abadi" (C-01, Active, Default User Activated), "PT Teknologi Maju" (C-02, Active, FAMS Grace, SAMS dan SIEM No Subscription, Default User Not Yet Activated), "PT Wahana Nusantara" (C-03, Suspended), "PT Karya Abadi" (C-04, Archived), "PT Maju Bersama" (C-06, Active Derived dari Partner CV Mitra Sejati, Distributor induk PT Distribusi Nusantara, Group Area Jakarta), "PT Baru Daftar" (C-09, tanpa subscription, Default User Not Yet Activated). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja; tidak memakai intercept, jam server, atau klien HTTP. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-234: Kelima tab Detail selalu tampil tanpa dipengaruhi plan, kuota, atau subscription

1. Ketik Search `PT Baru Daftar`, tekan Enter
2. Klik Company Name "PT Baru Daftar" untuk membuka Detail
3. Verifikasi navigasi tab memuat `Subscription | TAG | Hardware | Asset Control | Storage`
4. Klik Tab `Subscription`
5. Verifikasi Tab `Subscription` terbuka dan menampilkan empty state-nya
6. Klik Tab `TAG`
7. Verifikasi Tab `TAG` terbuka dan menampilkan empty state-nya
8. Klik Tab `Hardware`
9. Verifikasi Tab `Hardware` terbuka dan menampilkan empty state-nya
10. Klik Tab `Asset Control`
11. Verifikasi Tab `Asset Control` terbuka dan menampilkan empty state-nya
12. Klik Tab `Storage`
13. Verifikasi Tab `Storage` terbuka dan menampilkan empty state-nya

### TC-AC-ACC-235: Tab Subscription aktif pertama kali dan sub-tab FAMS aktif pertama untuk Principal

14. Kembali ke List lewat breadcrumb Client
15. Ketik Search `PT Sejahtera Abadi`, tekan Enter
16. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail
17. Verifikasi Tab `Subscription` aktif
18. Verifikasi sub-tab `FAMS | SAMS | SIEM` tampil
19. Verifikasi sub-tab `FAMS` aktif pertama
20. Kembali ke List lewat breadcrumb Client
21. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter
22. Klik Company Name "PT Teknologi Maju" untuk membuka Detail (FAMS Grace; SAMS dan SIEM No Subscription)
23. Verifikasi Tab `Subscription` aktif
24. Verifikasi sub-tab `FAMS | SAMS | SIEM` tampil (Principal melihat semua sub-tab)
25. Verifikasi sub-tab `FAMS` aktif pertama

### TC-AC-ACC-236: Detail Client Derived menampilkan badge "Derived from [nama]" dan Partner, Distributor, serta Group dari entitas induk

26. Kembali ke List lewat breadcrumb Client
27. Ganti isi Search dengan `PT Maju Bersama`, tekan Enter
28. Klik Company Name "PT Maju Bersama" untuk membuka Detail
29. Verifikasi badge `Derived from CV Mitra Sejati`
30. Verifikasi Section "Parent / Pengelola" menampilkan Partner "CV Mitra Sejati"
31. Verifikasi Section "Parent / Pengelola" menampilkan Distributor "PT Distribusi Nusantara"
32. Verifikasi Section "Parent / Pengelola" menampilkan Group "Area Jakarta" (di-resolve dari Anchor CV Mitra Sejati seperti Client non-Derived)

### TC-AC-ACC-239: Badge status entitas Active/Suspended/Archived memakai severity success/warning/dark

33. Kembali ke List lewat breadcrumb Client
34. Ganti isi Search dengan `PT Sejahtera Abadi`, tekan Enter
35. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail Client Active
36. Verifikasi badge status entitas `Active` berseverity success
37. Kembali ke List lewat breadcrumb Client
38. Klik sub-tab `Suspended`
39. Ketik Search `PT Wahana Nusantara`, tekan Enter
40. Klik Company Name "PT Wahana Nusantara" untuk membuka Detail Client Suspended
41. Verifikasi badge status entitas `Suspended` berseverity warning
42. Kembali ke List lewat breadcrumb Client
43. Klik sub-tab `Archived`
44. Ketik Search `PT Karya Abadi`, tekan Enter
45. Klik Company Name "PT Karya Abadi" untuk membuka Detail Client Archived
46. Verifikasi badge status entitas `Archived` berseverity dark

### TC-AC-ACC-240: Badge status Default User Activated dan Not Yet Activated serta tombol Resend Activation Email

47. Kembali ke List lewat breadcrumb Client
48. Klik sub-tab `Active`
49. Ketik Search `PT Sejahtera Abadi`, tekan Enter
50. Klik Company Name "PT Sejahtera Abadi" untuk membuka Detail lalu amati Section "Default User"
51. Verifikasi Section "Default User" "PT Sejahtera Abadi" menampilkan badge "Activated"
52. Verifikasi tombol `[Resend Activation Email]` tidak tampil pada Section "Default User" "PT Sejahtera Abadi"
53. Kembali ke List lewat breadcrumb Client
54. Ganti isi Search dengan `PT Teknologi Maju`, tekan Enter
55. Klik Company Name "PT Teknologi Maju" untuk membuka Detail lalu amati Section "Default User"
56. Verifikasi Section "Default User" "PT Teknologi Maju" menampilkan badge "Not Yet Activated"
57. Verifikasi tombol `[Resend Activation Email]` tampil pada Section "Default User" "PT Teknologi Maju"
58. Kembali ke List lewat breadcrumb Client
59. Ganti isi Search dengan `PT Baru Daftar`, tekan Enter
60. Klik Company Name "PT Baru Daftar" untuk membuka Detail lalu amati Section "Default User"
61. Verifikasi Section "Default User" "PT Baru Daftar" menampilkan badge "Not Yet Activated"
62. Verifikasi tombol `[Resend Activation Email]` tidak tampil pada Section "Default User" "PT Baru Daftar"

## Notes

- Spec melewati sekitar 35 langkah. Alasan: seluruh blok berupa pembacaan satu role pada satu surface, tiap blok berdiri sendiri (membuka Detail Client sendiri lewat Search), dan kegagalan keras satu blok tidak membuat blok lain kehilangan makna.
- Langkah Search nama Client sebelum membuka Detail adalah langkah penghubung untuk menemukan baris target (List berpaginasi 10 baris dan memuat fixture residen lain).
- Langkah "Kembali ke List lewat breadcrumb Client", klik sub-tab (`Active`, `Suspended`, `Archived`), dan Search adalah langkah penghubung (S-03).
- Temuan untuk QA (S-15): TC-239 mencantumkan Detail "PT Wahana Nusantara" pada Precondition tetapi Langkah menyebut "Client Active, Suspended, dan Archived" tanpa nama; spec memakai "PT Sejahtera Abadi" (C-01 Active), "PT Wahana Nusantara" (C-03 Suspended), dan "PT Karya Abadi" (C-04 Archived) dari Tabel A2. Post Condition seluruh TC `-` sehingga tidak diasersi. Tombol `[Resend Activation Email]` tidak tampil pada TC-240 diasersi sesudah badge Default User tampil pada Section yang sama.

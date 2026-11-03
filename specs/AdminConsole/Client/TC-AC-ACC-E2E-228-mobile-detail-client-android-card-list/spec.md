---
id: TC-AC-ACC-E2E-228-mobile-detail-client-android-card-list
title: "Mobile Detail Client (Android): Card Subscription dan License Quota serta Card List Tab TAG, Hardware, Asset Control, dan Storage"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-890
  - TC-AC-ACC-891
coverage:
  mobile: automated
---

# Mobile Detail Client (Android): Card Subscription dan License Quota serta Card List Tab TAG, Hardware, Asset Control, dan Storage

## Prerequisites

- Mode: FE+BE.
- Akun aktor (password hanya lewat `Spectra.env`, tidak ditulis di spec):

| Role | Email | Env var password |
|---|---|---|
| Total Control (Principal), A-01 | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login akun aktor pertama dilakukan di hook `before` spec ini; aplikasi Android dibuka pada halaman Admin Console > Client oleh hook `beforeEach` suite; langkah membuka Detail ada di `## Test Steps`.
- Flag Guided Tooltip halaman Client dan Detail Client (`guided_tooltip_seen_ac-client`, `guided_tooltip_seen_ac-client-detail`) disetel true untuk akun aktor oleh hook suite `before` dan dipulihkan oleh hook suite `after` (dinyatakan sekali di `suite.md`).
- Kemampuan teknis (platform mobile): aplikasi Android native dengan perangkat atau emulator Android disediakan tim FE (TC Manual Only (b) aplikasi native Android); perangkat fisik bersama sehingga suite berjalan serial (`parallel: false`).
- Data Pre-setup Residen (baca-saja, Tabel A2/A3): C-DTL-1 "PT Uji Tabel Detail" (License Quota FAMS Asset 650/320/330, Concurrent User 25/12/13, Addon: Maintenance 50/50/0, Addon: Tracking 20/5/15 (Total/Used/Available)) dan C-01 "PT Sejahtera Abadi" (Station Asset Control "Gerbang Gudang A", "Gerbang Gudang B", "Gerbang Lama"). Data Pre-setup Residen (kelas baca-saja, Tabel A2/A3) dibaca dengan nama literal tanpa suffix sebagai pengecualian S-12 atas keputusan pengguna (Q5); spec tidak menulis, mengubah, atau menghapusnya.
- Kemampuan teknis: browser web saja. Spec read-only dan tidak membuat data.

## Test Steps

### TC-AC-ACC-890: Mobile: Tab Subscription di Detail menampilkan card per produk dan license quota dalam baris

1. Buka Detail "PT Uji Tabel Detail" (aplikasi Android)
2. Buka Tab `Subscription` sub-tab `FAMS`
3. Verifikasi Section Subscription Details tampil sebagai card per produk (bukan tabel)
4. Scroll ke Section "License Quota"
5. Verifikasi License Quota baris Asset: Total 650, Used 320, Available 330
6. Verifikasi License Quota baris Concurrent User: Total 25, Used 12, Available 13
7. Verifikasi License Quota baris Addon: Maintenance: Total 50, Used 50, Available 0
8. Verifikasi License Quota baris Addon: Tracking: Total 20, Used 5, Available 15

### TC-AC-ACC-891: Mobile: Tab TAG, Hardware, Asset Control, dan Storage menampilkan card list sebagai pengganti tabel

9. Buka Detail "PT Sejahtera Abadi" (aplikasi Android)
10. Buka Tab `TAG` lalu scroll Section Quota dan Section Purchase History TAG
11. Verifikasi Tab `TAG`: Quota dan Purchase History TAG tampil sebagai card list satu card per baris data
12. Verifikasi Tab `TAG` tidak menampilkan tabel
13. Buka Tab `Hardware` lalu scroll Section Hardware List, Section Quota, dan Section Purchase History Hardware
14. Verifikasi Tab `Hardware`: Hardware List, Quota, dan Purchase History Hardware tampil sebagai card list satu card per baris data
15. Verifikasi Tab `Hardware` tidak menampilkan tabel
16. Buka Tab `Asset Control` lalu scroll Section Station List
17. Verifikasi Tab `Asset Control`: Station List tampil sebagai card list dengan tiga card ("Gerbang Gudang A", "Gerbang Gudang B", "Gerbang Lama")
18. Verifikasi Tab `Asset Control` tidak menampilkan tabel
19. Buka Tab `Storage` lalu scroll Section Quota dan Section Purchase History Storage
20. Verifikasi Tab `Storage`: Quota dan Purchase History Storage tampil sebagai card list satu card per baris data
21. Verifikasi Tab `Storage` tidak menampilkan tabel

## Notes

- Spec berjalan di aplikasi Android (`coverage.mobile`); tidak ada variasi web. Absence "tidak menampilkan tabel" didahului Verifikasi card list pada tab yang sama sebagai anchor positif (bagian 8b butir 2).
- Langkah "Buka Detail ... (aplikasi Android)" mengikuti redaksi TC; cara membuka Detail pada aplikasi Android (mis. Search dan klik Company Name) tidak dirinci TC.
- Temuan untuk QA (S-15): TC-890/891 menyebut aplikasi Android untuk Admin Console > Client; PRD Client dan TC lain memperlakukan Detail sebagai halaman web, dan viewport mobile web disebut pula pada TC-862/863. Perlu dikonfirmasi QA apakah yang diuji aplikasi Android native atau viewport mobile web. Post Condition `-`.

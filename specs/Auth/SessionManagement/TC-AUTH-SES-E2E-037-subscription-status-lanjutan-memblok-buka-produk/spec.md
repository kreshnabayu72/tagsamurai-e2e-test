---
id: TC-AUTH-SES-E2E-037-subscription-status-lanjutan-memblok-buka-produk
title: "Subscription Status Lanjutan (Purge, Deleted, dan Status Non-Aktif Lain) Memblok Pembukaan Produk Baru"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-114
  - TC-AUTH-SES-115
  - TC-AUTH-SES-274
  - TC-AUTH-SES-275
  - TC-AUTH-SES-276
  - TC-AUTH-SES-277
  - TC-AUTH-SES-278
coverage:
  web: automated
---

# Subscription Status Lanjutan (Purge, Deleted, dan Status Non-Aktif Lain) Memblok Pembukaan Produk Baru

## Prerequisites

- Mode: FE+BE.
- Tiga Client uji status subscription (Tabel Data Uji Pre-setup #14), masing-masing dengan subscription Fixed Asset Active di awal spec: Client Purge uji (user TC-AUTH-SES-114), Client Deleted uji (user TC-AUTH-SES-115), dan Client uji (kelima user lainnya). Purge dan Deleted adalah status terminal yang tidak dapat dipulihkan, sehingga tiap status memakai Client sendiri yang disediakan tim BE per run dan tidak dipakai ulang. Status subscription Fixed Asset tiap Client dikondisikan BE per TC lewat langkah eksplisit "Atur status subscription ..." oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`. Status Purge dan Deleted dicapai lewat lifecycle subscription; status Waiting for Approval, Pending, Cancelled, Rejected, dan Converted di-seed BE (disediakan tim BE). Jam server uji tidak digeser karena menggeser jam membuat sesi platform seluruh user uji melewati batas idle.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Expired/uji (Tabel Data Uji Pre-setup #31), kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run; `Reza Lestari` milik Client Purge uji, `Sari Pratama` milik Client Deleted uji, kelima user lain milik Client uji. Tidak ada sesi-produk Active milik user mana pun:
  - TC-AUTH-SES-114: `Reza Lestari` (`rezalestari+{runId}-037@qwertysystem.net`)
  - TC-AUTH-SES-115: `Sari Pratama` (`saripratama+{runId}-037@qwertysystem.net`)
  - TC-AUTH-SES-274: `Agus Lestari` (`aguslestari+{runId}-037@qwertysystem.net`)
  - TC-AUTH-SES-275: `Rina Pratama` (`rinapratama+{runId}-037@qwertysystem.net`)
  - TC-AUTH-SES-276: `Hendra Ramadhan` (`hendraramadhan+{runId}-037@qwertysystem.net`)
  - TC-AUTH-SES-277: `Maya Wulandari` (`mayawulandari+{runId}-037@qwertysystem.net`)
  - TC-AUTH-SES-278: `Fajar Hidayat` (`fajarhidayat+{runId}-037@qwertysystem.net`)
- Sesi platform web aktif per user, di Portal — Product Hub, dibuat di hook `before` lewat login API. Browser A pada tiap TC = konteks browser yang memuat sesi platform user TC bersangkutan (satu konteks per user, dibuat di `before`).
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): pulihkan status subscription Fixed Asset Client uji ke Active lewat seed yang disediakan tim BE; Client Purge uji dan Client Deleted uji tidak dipulihkan (status terminal); akhiri semua sesi seed, tutup semua konteks browser, hapus ketujuh user (untuk Client yang sudah Purge atau Deleted, pembersihan mengikuti seed yang disediakan tim BE).
- Suite berjalan serial (`parallel: false`); state global yang diubah: status subscription Fixed Asset Client uji (dipulihkan di hook `after`) serta Client Purge uji dan Client Deleted uji (status terminal, tidak dipulihkan, habis pakai per run).
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness h: state tenant): pengaturan status subscription (termasuk status yang di-seed BE) per langkah oleh akun principal Admin Console; satu konteks browser per user uji; pembacaan status HTTP response request pembukaan sesi-produk Fixed Asset di Browser A; pembacaan sesi-produk milik user uji dari sisi backend (ada atau tidak ada sesi-produk Fixed Asset untuk user itu).
- Akun yang dipakai: user uji masing-masing TC pada Browser A; akun aktor principal Admin Console (langkah "Atur status subscription ..."); akun aktor Total Control (Global Settings) dengan scope Client Expired/uji (#31, seeding di hook `before`).

## Test Steps

### TC-AUTH-SES-114: Buka produk baru saat subscription Purge memunculkan Popup Subscription Not Active

1. Atur status subscription Fixed Asset Client Purge uji menjadi Purge
2. Di Browser A (sesi `Reza Lestari`) klik card Fixed Asset → Popup muncul
3. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
4. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
5. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Reza Lestari`
6. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-115: Buka produk baru saat subscription Deleted memunculkan Popup Subscription Not Active

7. Atur status subscription Fixed Asset Client Deleted uji menjadi Deleted
8. Di Browser A (sesi `Sari Pratama`) klik card Fixed Asset → Popup muncul
9. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
10. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
11. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Sari Pratama`
12. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-274: Buka produk baru saat subscription Waiting for Approval memunculkan Popup Subscription Not Active

13. Atur status subscription Fixed Asset Client uji menjadi Waiting for Approval
14. Di Browser A (sesi `Agus Lestari`) klik card Fixed Asset → Popup muncul
15. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
16. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
17. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Agus Lestari`
18. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-275: Buka produk baru saat subscription Pending memunculkan Popup Subscription Not Active

19. Atur status subscription Fixed Asset Client uji menjadi Pending
20. Di Browser A (sesi `Rina Pratama`) klik card Fixed Asset → Popup muncul
21. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
22. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
23. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Rina Pratama`
24. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-276: Buka produk baru saat subscription Cancelled memunculkan Popup Subscription Not Active

25. Atur status subscription Fixed Asset Client uji menjadi Cancelled
26. Di Browser A (sesi `Hendra Ramadhan`) klik card Fixed Asset → Popup muncul
27. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
28. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
29. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Hendra Ramadhan`
30. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-277: Buka produk baru saat subscription Rejected memunculkan Popup Subscription Not Active

31. Atur status subscription Fixed Asset Client uji menjadi Rejected
32. Di Browser A (sesi `Maya Wulandari`) klik card Fixed Asset → Popup muncul
33. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
34. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
35. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Maya Wulandari`
36. Verifikasi Halaman Fixed Asset tidak dimuat

### TC-AUTH-SES-278: Buka produk baru saat subscription Converted memunculkan Popup Subscription Not Active

37. Atur status subscription Fixed Asset Client uji menjadi Converted
38. Di Browser A (sesi `Fajar Hidayat`) klik card Fixed Asset → Popup muncul
39. Verifikasi Popup "Subscription Not Active" tampil dengan Body "Your subscription is not active. Please contact your administrator."
40. Verifikasi Server menjawab 403 pada request pembukaan sesi-produk Fixed Asset
41. Verifikasi Sesi-produk Fixed Asset tidak dibuat untuk `Fajar Hidayat`
42. Verifikasi Halaman Fixed Asset tidak dimuat

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness h (state tenant). Spec ini melewati batas sekitar 35 langkah karena tujuh TC berpola identik (satu status per TC); bagian sesudah tiap TC tidak bergantung pada TC sebelumnya.
- Urutan mengikuti TC sumber (114, 115, 274, 275, 276, 277, 278); tidak ada penyimpangan (S-05, S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah "Atur status subscription ..." (langkah 1, 7, 13, 19, 25, 31, 37) mengondisikan state tenant per TC.
- Expected c tiap TC ("Tidak ada entri log baru" di `Activity Log > Session` dan User Log) adalah asersi absence; tidak diasersikan di spec ini dan dirujuk ke spec absence `TC-AUTH-SES-E2E-068-absence-subscription-tidak-aktif` untuk TC-AUTH-SES-114, 115, dan 274 s.d. 278 (S-05). Pada TC-AUTH-SES-274 s.d. 278 butir ini bertanda `[DEFERRED]` karena surface `Activity Log > Session` milik Fixed Asset adalah forward-dependency (NC-15).
- Temuan untuk QA: (1) TC-AUTH-SES-114, 115, 274 s.d. 278 menyebut "Client dengan subscription ... berstatus X (Tabel Data Uji Pre-setup #14)" tanpa menyebut cara memicu status itu; spec memakai Client uji (status non-terminal), Client Purge uji, dan Client Deleted uji, dengan status diatur per langkah. (2) Expected b tiap TC memuat tiga klausa (403, sesi-produk tidak dibuat, halaman tidak dimuat); spec memecahnya menjadi tiga `Verifikasi`. Cara membaca "sesi-produk tidak dibuat" tidak disebut TC; spec mengandalkan pembacaan dari sisi backend (Prerequisites). (3) TC-AUTH-SES-115 (Deleted) dan 114 (Purge) mengasumsikan user masih dapat login dan memegang sesi platform pada Client berstatus itu; bila pada status tersebut login ditolak, precondition TC tidak dapat dibentuk dan sesi platform perlu dibuat sebelum status diubah. (4) Pre-setup #14 tidak memisahkan Client per status terminal dan Pre-setup #31 hanya mendefinisikan akun aktor Total Control untuk scope Client Expired/uji; spec memakai Client Purge uji dan Client Deleted uji terpisah (status Purge dan Deleted tidak dapat dipulihkan) dan mengasumsikan scope akun aktor mencakup keduanya. (5) Pemulihan status subscription ke Active untuk status non-terminal tidak didefinisikan TC maupun PRD License Allocation Subscription (rantai status satu arah); spec menuliskannya sebagai seed yang disediakan tim BE.

---
id: TC-AC-CS-E2E-054-state-tenant-client-suspended-dan-expired-pada-add-renew
title: "State Tenant: Client Suspended dan Expired pada Add, Renew, Activate Trial"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-196
  - TC-AC-CS-197
  - TC-AC-CS-198
  - TC-AC-CS-528
  - TC-AC-CS-529
coverage:
  web: automated
---

# State Tenant: Client Suspended dan Expired pada Add, Renew, Activate Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan langsung PT Maju Bersama; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed A dan B): Client `Toko Rejeki Suspended+{runId}-054` (status Suspended) dengan term paid FAMS Active (Subscription ID seed A; padanan Pre-setup #45 dan #117); Client `Toko Rejeki Expired+{runId}-054` (status Expired) dengan term paid FAMS Active (Subscription ID seed B; padanan Pre-setup #46 dan #120). Tanggal acuan uji `19/08/26`.
- Data Dinamis: Term SAMS yang dibuat TC-AC-CS-528 dan Renewal TC-AC-CS-529 serta perubahan status Client seed hanya mengenai data seed milik spec ini dan dihapus bersama Client seed di hook `after` (fixture backend pemulihan state, disediakan tim FE/BE). Pre-setup #45, #46, #117, #120 tidak disentuh.
- Kemampuan teknis (disediakan tim FE/BE): mengatur status Client (Active, Suspended, Expired) lewat fixture backend; pelaku Suspend dari sesi API aktor (kelas h, pemicu); fixture waktu tanggal acuan `19/08/26` (dipulihkan di hook `after`).

## Test Steps

### TC-AC-CS-196: Client Suspended menampilkan V-19 inline saat dipilih

1. Klik `[+ Activate Trial]`
2. Buka dropdown Client lalu pilih `Toko Rejeki Suspended+{runId}-054`
3. Verifikasi Client Suspended tetap tampil di dropdown Client
4. Verifikasi error inline "Cannot activate trial for a suspended client" tampil pada field Client segera setelah dipilih

### TC-AC-CS-197: Submit Activate Trial untuk Client Suspended ditolak ulang oleh server

5. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
6. Pulihkan Client `Toko Rejeki Suspended+{runId}-054` ke status Active lewat fixture backend, lalu buka Allocation > Client Subscription tab Current
7. Klik `[+ Activate Trial]`
8. Pilih Client `Toko Rejeki Suspended+{runId}-054`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
9. Suspend Client `Toko Rejeki Suspended+{runId}-054` lewat sesi API aktor hingga status Suspended tersimpan
10. Klik `[Submit]`
11. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." dan bukan pesan V-19
12. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
13. Ketik Search `Toko Rejeki Suspended+{runId}-054`, tekan Enter
14. Verifikasi baris term paid Subscription ID seed A tampil
15. Verifikasi tidak ada baris Trial untuk Client `Toko Rejeki Suspended+{runId}-054`

### TC-AC-CS-198: Activate Trial untuk Client Expired ditolak server dengan toast baku

16. Klik `✕` pada Search, tekan Enter
17. Klik `[+ Activate Trial]`
18. Pilih Client `Toko Rejeki Expired+{runId}-054`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
19. Klik `[Submit]`
20. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." dan bukan pesan V-19
21. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
22. Ketik Search `Toko Rejeki Expired+{runId}-054`, tekan Enter
23. Verifikasi baris term paid Subscription ID seed B tampil
24. Verifikasi tidak ada baris Trial untuk Client `Toko Rejeki Expired+{runId}-054`

### TC-AC-CS-528: Add Subscription tetap diizinkan pada Client Suspended

25. Pulihkan Client `Toko Rejeki Suspended+{runId}-054` ke status Suspended lewat fixture backend, klik `✕` pada Search, tekan Enter
26. Klik `[+ Subscription]`
27. Pilih Client `Toko Rejeki Suspended+{runId}-054`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
28. Klik `[Submit]`
29. Verifikasi toast sukses "Success, subscription has been added."
30. Ketik Search `Toko Rejeki Suspended+{runId}-054`, tekan Enter
31. Verifikasi term SAMS Client `Toko Rejeki Suspended+{runId}-054` berstatus Active

### TC-AC-CS-529: Renew tetap diizinkan pada Client Expired

32. Klik `✕` pada Search, tekan Enter
33. Ketik Search `Toko Rejeki Expired+{runId}-054`, tekan Enter
34. Klik `Renew` pada baris Subscription ID seed B Client `Toko Rejeki Expired+{runId}-054`, isi Duration `1`
35. Klik `[Submit]`
36. Verifikasi toast sukses Renew tampil
37. Verifikasi tidak ada penolakan oleh state Expired (tidak ada toast error "Changes can't be saved while this workspace is suspended or expired.")

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-196 (kasus tanpa submit) paling awal pada satu form; TC-AC-CS-528 dan TC-AC-CS-529 (aksi sukses yang mengubah data) paling akhir.
- Perubahan status Client dilakukan lewat fixture backend dan sesi API aktor; pelaku kedua lewat sesi API bukan konteks kedua dan tidak memakai P-2 (KEPUTUSAN 2026-10-30). Spec ini seluruhnya kelas h (state tenant).
- Alasan melewati sekitar 35 langkah bila dihitung penuh: semua blok satu kelas harness (h, state tenant) pada Activate Trial, Add, dan Renew dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): `✕` dan `[Leave]` menutup form dirty (S-08, S-09); Search untuk menemukan baris target (R-16); pemulihan status Client seed oleh fixture; Search Client seed Expired sebelum aksi `Renew` pada baris seed (R-16).
- Anchor absence (bagian 8b butir 2): ketiadaan baris Trial didahului Verifikasi baris term paid milik Client yang sama tampil pada surface yang sama.
- Temuan untuk QA: (1) TC-AC-CS-528 menyebut Client `Toko Rejeki Suspended+{runId}-054` "tanpa term" padahal Pre-setup #117 memuat term paid FAMS Active pada Client yang sama (seed spec ini meniru keadaan itu); spec menambah term Product SAMS dan tidak bergantung pada kosongnya term. (2) TC-AC-CS-528 butir c ("Akses fitur Client tetap terblokir oleh state Suspended sebagai lapisan terpisah") tidak punya langkah observasi sehingga tidak diasersi. (3) TC-AC-CS-529 butir a tidak menyebut teks toast sukses Renew; spec mengasersi toast sukses Renew tampil tanpa teks. (4) TC-AC-CS-197 mengharuskan Client Active saat dipilih lalu di-Suspend; spec memulihkan status Active dulu karena Client seed dibuat berstatus Suspended.

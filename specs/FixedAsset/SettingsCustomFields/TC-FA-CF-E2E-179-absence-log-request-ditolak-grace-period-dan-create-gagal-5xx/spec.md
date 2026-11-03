---
id: TC-FA-CF-E2E-179-absence-log-request-ditolak-grace-period-dan-create-gagal-5xx
title: "Absence Log: Request Tulis Field Accounting Ditolak Saat Grace Period dan Create Gagal 5xx"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-665
  - TC-FA-CF-666
  - TC-FA-CF-184
coverage:
  web: automated
---

# Absence Log: Request Tulis Field Accounting Ditolak Saat Grace Period dan Create Gagal 5xx

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Grace `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Grace (Pre-setup #1 dan #25). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_GRACE_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Email akun ini tidak tertulis di Pre-setup TC; disediakan tim FE. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun kedua (ganti akun eksplisit pada langkah 33 dan 34): Total Control Company Alpha, pengguna Sarah Johnson (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha; login UI dengan `Spectra.env.FA_TC_PASSWORD`. Dipakai TC-FA-CF-184. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Company Grace (Pre-setup #25): FA-7 sempat aktif lalu diturunkan ke None efektif T-0 dengan Grace Period berjalan (T+10 hari); field Accounting `Cost Center` (Text, General, Active, Required Yes) dan `Asset Tag Class` (Text, General, Inactive) tersimpan. Company Alpha (plan Professional, lisensi FA-7 aktif; Pre-setup #11) dengan baseline tab General delapan field (Pre-setup #12) yang dirujuk lewat fixture `Fixture.faCustomFields.baselineGeneral`.
- Data Dinamis: Field Name payload yang ditolak atau digagalkan, tidak pernah tersimpan: `Grace Create {runId}-179` dan `Fail 5xx {runId}-179`.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP untuk request langsung ke server dengan token akun aktor (login API password); asersi request langsung hanya status respons dan state data (8b butir 1). `Spectra.intercept()` untuk memaksa respons 500 pada Create (Pre-setup #26), dilepas segera setelah pemicu (S-09).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah dan isi entri Changelog tab General dan Accounting, System Log pengguna aktor, dan Activity Log untuk baseline dan perbandingan; total entri tidak diasersi sebagai angka absolut, hanya selisih terhadap baseline (S-12). Seed reset Company untuk memulihkan baseline.
- State global: tidak ada yang diubah. Seed reset Company memulihkan baseline di hook `before` dan `after`.
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-665: Request tulis single atas field Accounting selama Grace Period ditolak 403

1. Catat jumlah entri Changelog tab Accounting, System Log aktor, dan Activity Log Company Grace sebagai baseline (kemampuan baca disediakan tim FE/BE)
2. Kirim request Create field grup Accounting (Field Name `Grace Create {runId}-179`) langsung ke server
3. Verifikasi server merespons 403 Forbidden
4. Kirim request Edit untuk `Cost Center` langsung ke server
5. Verifikasi server merespons 403 Forbidden
6. Kirim request Deactivate untuk `Cost Center` dan request Activate untuk `Asset Tag Class` langsung ke server
7. Verifikasi server merespons 403 Forbidden untuk request Deactivate dan request Activate
8. Kirim request Delete untuk `Cost Center` langsung ke server
9. Verifikasi server merespons 403 Forbidden
10. Muat ulang (F5) halaman Settings > Custom Fields lalu klik tab `Accounting`
11. Verifikasi tab `Accounting` memuat baris `Cost Center` dan `Asset Tag Class`
12. Verifikasi tidak ada field baru: tab `Accounting` hanya memuat `Cost Center` dan `Asset Tag Class`
13. Verifikasi `Cost Center` tidak berubah: switch Active ON, Data Type `Text`, Scope `General`, Required `Yes`
14. Verifikasi `Asset Tag Class` tidak berubah: switch Active OFF, Data Type `Text`, Scope `General`
15. Buka Modal Changelog tab Accounting dan hitung ulang jumlah entri
16. Verifikasi jumlah entri Changelog tab Accounting sama dengan baseline (tidak ada entri baru)
17. Buka System Log aktor Company Grace dan hitung ulang jumlah entri
18. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak ada entri baru)
19. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
20. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

### TC-FA-CF-666: Request bulk atas field Accounting selama Grace Period ditolak 403

21. Catat jumlah entri Modal Changelog tab Accounting, System Log aktor, dan Activity Log Company Grace sebagai baseline
22. Kirim request Bulk Deactivate untuk `Cost Center` langsung ke server
23. Verifikasi server merespons 403 Forbidden
24. Kirim request Bulk Delete untuk `Cost Center` dan `Asset Tag Class` langsung ke server
25. Verifikasi server merespons 403 Forbidden
26. Verifikasi tidak ada perubahan sebagian pada `Cost Center` dan `Asset Tag Class` (dibaca lewat fixture BE)
27. Buka Modal Changelog tab Accounting dan hitung ulang jumlah entri
28. Verifikasi jumlah entri Changelog tab Accounting sama dengan baseline (tanpa entri log)
29. Buka System Log aktor Company Grace dan hitung ulang jumlah entri
30. Verifikasi jumlah entri System Log aktor sama dengan baseline (tanpa entri log)
31. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
32. Verifikasi jumlah entri Activity Log sama dengan baseline (tanpa entri log)

### TC-FA-CF-184: Create gagal 5xx menampilkan toast error, modal tetap terbuka, input dipertahankan, tombol aktif kembali

33. Ganti akun: `Logout` dari Total Control Company Grace
34. Login sebagai Total Control Company Alpha (Pre-setup #1) dengan `Spectra.env.FA_TC_PASSWORD`
35. Buka Fixed Asset > Settings > Custom Fields (tab General)
36. Catat jumlah entri Modal Changelog tab General, System Log `Sarah Johnson`, dan Activity Log Company Alpha sebagai baseline, lalu kembali ke Fixed Asset > Settings > Custom Fields (tab General)
37. Klik `[+ Custom Field]`
38. Isi Field Name `Fail 5xx {runId}-179` dan Data Type `Text`
39. Intersep respons Create dengan 500
40. Klik `[Submit]`
41. Verifikasi toast error `Error, failed to create custom field.` tampil
42. Verifikasi modal tetap terbuka
43. Verifikasi input dipertahankan (Field Name `Fail 5xx {runId}-179` dan Data Type `Text`)
44. Verifikasi `[Submit]` aktif kembali untuk retry
45. Tunggu 10 detik
46. Verifikasi toast error tetap tampil (bertahan sampai di-dismiss)
47. Lepas intersepsi
48. Tutup toast error
49. Klik icon close `[✕]`
50. Verifikasi dialog `Unsaved Changes` tampil
51. Klik `[Leave]`
52. Ketik Search `Fail 5xx {runId}-179`, tekan Enter
53. Verifikasi tabel tidak memuat field `Fail 5xx {runId}-179` (empty state `No results found`)
54. Klik `(←)` pada kotak Search
55. Buka Modal Changelog tab General dan hitung ulang jumlah entri
56. Verifikasi jumlah entri Changelog tab General sama dengan baseline (tidak ada entri log)
57. Buka Settings > User > Detail pengguna `Sarah Johnson` > Tab System Log dan hitung ulang jumlah entri
58. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline (tidak ada entri log)
59. Buka Reports & Logs > Activity Log > Tab User Action dan hitung ulang jumlah entri
60. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri log)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas 35 langkah: spec memuat 60 langkah bernomor; langkah blok baca-log berpola (buka surface, hitung entri, `Verifikasi` jumlah; 18 langkah, nomor 15 sampai 20, 27 sampai 32, dan 55 sampai 60) tidak dihitung pada smell (bagian 3), sehingga hitungan efektif 42 langkah. Spec dipertahankan karena semua blok satu kelas (absence log, kelas g), tiap TC punya aksi, user, dan baseline sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CF-184 membawa Verifikasi toast, modal, dan input sebagai Expected a dan b-nya sendiri sehingga ditulis lengkap.
- P-5 (a): spec absence kelas g; pemicu kelas a (request langsung), kelas b (respons 500 pada Create lewat intersep), dan kelas h (Grace Period) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; user dan baseline tiap TC sendiri (S-12). Company Grace memakai akun dan state sendiri; TC absence Company lain ada di spec 132 (TC-FA-CF-505, 514, 557, 572, 575, 576) dan spec 133 (TC-FA-CF-555, 584, 659).
- Anchor positif (8b butir 2): status respons 403, baris `Cost Center` dan `Asset Tag Class` tampil di tab `Accounting`, toast error dan modal Create yang tetap terbuka pada TC-FA-CF-184, serta jumlah entri awal yang dicatat pada baseline tiap TC. Absence field baru memakai empty state `No results found` sebagai anchor.
- K-1: TC-FA-CF-665 dan 666 kelas a dengan Expected respons API tetap masuk spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec.
- S-05: asersi absence log TC-FA-CF-666 dan 184 hanya ada di spec ini; spec 147 (TC-FA-CF-666) dan spec 160 (TC-FA-CF-184) mencatat rujukan ke sini di `## Notes`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 33 dan 34 (ganti akun eksplisit ke Company Alpha), langkah 35 (membuka halaman Custom Fields), baseline, pengiriman request langsung, pelepasan intersepsi (langkah 47), menutup toast error (langkah 48), menutup form dirty (langkah 49 sampai 51, S-08), Search (R-16), dan langkah buka surface serta hitung ulang jumlah entri. Langkah 45 adalah jeda nyata pendek di bawah 30 detik (bagian 6).
- Temuan untuk QA:
  - TC-FA-CF-665 Expected b menyebut `nilai` tidak berubah; nilai aset `Cost Center` (`CC-100` pada A1) tidak teramati dari halaman Custom Fields dan TC tidak memberi langkah observasi; spec mengasersi status dan konfigurasi pada tabel saja.
  - TC-FA-CF-665 tidak menyebut payload request Create, Edit, Deactivate, Activate, dan Delete; spec menyebut jenis request persis seperti TC tanpa mengarang endpoint atau body.
  - TC-FA-CF-665 Expected c dan TC-FA-CF-666 hanya menyebut "ketiga surface log"; spec membaca Changelog tab Accounting karena field yang diuji ada di grup Accounting.
  - TC-FA-CF-184 butir c ("tidak ada entri log") tanpa path menu System Log aktor dan Activity Log; spec membaca System Log `Sarah Johnson` pada Detail pengguna dan Activity Log pada Tab User Action.
  - Email akun Total Control Company Grace tidak tertulis di Pre-setup TC; env var `FA_TC_GRACE_PASSWORD` disediakan tim FE.

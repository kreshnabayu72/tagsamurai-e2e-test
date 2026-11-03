---
id: TC-AC-LA-E2E-035-opsi-target-term-eligible
title: "Opsi Target: Term Paid Active dan Pending, Client-wide, Free, Trial, dan Callout"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-123
  - TC-AC-LA-124
  - TC-AC-LA-125
  - TC-AC-LA-126
  - TC-AC-LA-127
  - TC-AC-LA-128
coverage:
  web: automated
---

# Opsi Target: Term Paid Active dan Pending, Client-wide, Free, Trial, dan Callout

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Pre-setup #1), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, dan ID Subscription.
- Data Pre-setup (hanya dibaca): Apotek Lama (#28, hanya term Paid Expired dan Canceled), Toko Serba Ada (#21, `SUBS-20250201-J7K8L` Active dan `SUBS-20260819-00001` Pending), Warung Gratis (#26, hanya FAMS Free Active), Toko Percobaan (#27, hanya FAMS Trial Active), Toko Menunggu Aktif (#72, hanya term Paid Pending `SUBS-20270101-00001`), Klinik Harapan Bunda (#24, dua Subscription Paid Active).
- Data Dinamis: tidak ada; tidak ada `[Submit]` pada spec ini.
- State global: tidak ada yang diubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik `[+ Allocation]`

### TC-AC-LA-123: Client tanpa term Paid Active maupun Pending

2. Pilih Client `Apotek Lama`
3. Verifikasi Target Disabled
4. Verifikasi info callout `This client has no active or pending paid subscription.`

### TC-AC-LA-124: Opsi Target memuat term Paid Active dan Pending ditambah Client-wide

5. Pilih Client `Toko Serba Ada`
6. Buka dropdown Target
7. Verifikasi opsi `SUBS-20250201-J7K8L · FAMS · Active` dan `SUBS-20260819-00001 · FAMS · Pending` tampil dengan badge status
8. Verifikasi opsi `Client-wide` tampil
9. Verifikasi tidak ada opsi term Canceled atau Expired

### TC-AC-LA-125: Subscription Free tidak muncul sebagai Target

10. Pilih Client `Warung Gratis`
11. Verifikasi Target Disabled sehingga term Free tidak muncul sebagai opsi Target untuk Type apa pun
12. Verifikasi info callout `This client has no active or pending paid subscription.`
13. Hover kontrol Target
14. Verifikasi tooltip S-07 tidak tampil

### TC-AC-LA-126: Subscription Trial tidak muncul sebagai Target

15. Pilih Client `Toko Percobaan`
16. Verifikasi Target Disabled sehingga term Trial tidak muncul sebagai opsi Target
17. Verifikasi info callout `This client has no active or pending paid subscription.`
18. Hover kontrol Target
19. Verifikasi tooltip S-07 tidak tampil

### TC-AC-LA-127: Client-wide disabled dengan tooltip S-07 saat Client hanya punya term Paid Pending

20. Pilih Client `Toko Menunggu Aktif`
21. Buka dropdown Target
22. Verifikasi Target Enabled dan memuat opsi `SUBS-20270101-00001 · FAMS · Pending`
23. Verifikasi opsi `Client-wide` Disabled
24. Hover opsi `Client-wide`
25. Verifikasi tooltip `Client-wide allocation requires at least one active paid subscription.`

### TC-AC-LA-128: Client-wide tersedia bila Client punya minimal satu Subscription Paid Active

26. Pilih Client `Klinik Harapan Bunda`
27. Buka dropdown Target
28. Verifikasi opsi `Client-wide` aktif
29. Pilih Target `Client-wide`
30. Buka dropdown Type
31. Verifikasi dropdown Type hanya memuat `Asset Control Station` dan `Storage`
32. Klik `[✕]` pada header
33. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
34. Klik `[Leave]`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 1 kali, kejadian menutup 1 (langkah 32 sampai 34). Semua blok satu topik (opsi Target per kondisi Client) dan berdiri sendiri: mengganti Client mereset Target (TC-AC-LA-136), sehingga tiap blok dimulai dari state yang setara dengan form baru; spec ini 34 langkah dan tidak melewati ambang.
- Langkah penghubung (S-03): langkah 6, 21, dan 27 (membuka dropdown agar opsi dapat diamati), langkah 13 dan 18 (hover kontrol Target agar absence tooltip dapat diasersi), langkah 29 (memilih Target agar dropdown Type dapat dibuka), dan langkah 32 sampai 34 (menutup form dirty, S-08).
- Asersi absence langkah 9, 14, dan 19 didahului Verifikasi pada surface yang sama (opsi term lain pada langkah 7, callout pada langkah 12 dan 17; bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-125 dan TC-AC-LA-126 Expected a ("Term Free/Trial tidak muncul sebagai opsi Target") tidak dapat diamati pada Target yang Disabled seluruhnya (Expected b); spec memakai Target Disabled sebagai bukti tidak ada opsi.
  - TC-AC-LA-125 dan TC-AC-LA-126 Expected c ("Tidak ada tooltip S-07 yang diharapkan") ditulis sebagai catatan penjelas, bukan hasil yang dapat diamati; spec mengasersi tooltip S-07 tidak tampil saat hover kontrol Target.
  - TC-AC-LA-125 dan TC-AC-LA-126 tidak menyebut ID term Free dan Trial, sehingga tidak ada asersi atas ID tertentu.
  - TC-AC-LA-124 Expected a menyebut "badge status" tanpa menyebut warna atau severity badge; hanya keberadaan badge yang diasersi.

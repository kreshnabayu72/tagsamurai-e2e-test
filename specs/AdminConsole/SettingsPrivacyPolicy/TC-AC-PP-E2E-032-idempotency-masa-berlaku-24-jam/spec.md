---
id: TC-AC-PP-E2E-032-idempotency-masa-berlaku-24-jam
title: "Idempotency Publish: Masa Berlaku Key 24 Jam dan Batas Tepat 24 Jam"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-94
  - TC-AC-PP-212
coverage:
  web: automated
---

# Idempotency Publish: Masa Berlaku Key 24 Jam dan Batas Tepat 24 Jam

## Prerequisites

- Mode: FE+BE (kelas d, harness waktu: jam server digeser; intercept parsial di atas backend nyata dan asersi state backend).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe`, Version 2 `John Doe`, Version 1 `Jane Smith` akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Fixture BE juga dipakai untuk mengembalikan dataset di antara dua blok TC (langkah penghubung).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Spec tidak mengubahnya.
- Kemampuan teknis:
  - Fixture BE untuk membuat ulang dataset Riwayat A.
  - Fixture waktu untuk mengatur jam server. Masa berlaku key adalah TTL yang dihitung murni di server dan tidak diamati lewat countdown UI, sehingga hanya jam server yang diatur; jam browser tidak diubah. TC-AC-PP-94 memajukan jam server 24 jam 1 menit; TC-AC-PP-212 mengatur jam server secara absolut ke waktu tersimpannya `Version 4` ditambah tepat 24 jam (dibekukan, bukan digeser relatif, karena batas eksak). Jam server dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah) dan juga di langkah spec sebelum blok berikutnya.
  - `Spectra.intercept()` untuk menangkap permintaan Publish pertama (mengamati idempotency key K dan isi permintaan) tanpa mengubahnya, dan untuk menimpa key pada permintaan berikutnya dengan K (TC-AC-PP-94).
  - Klien HTTP dengan token sesi Total Control untuk mengirim ulang permintaan Publish dengan key K (TC-AC-PP-212 langkah 3).
  - Sumber waktu simpan `Version 4` (T4) yang dapat dibaca spec dengan ketelitian detik (kebutuhan tim FE; Published At di UI hanya menampilkan tanggal tanpa jam, sehingga T4 tidak bisa dibaca dari layar), misalnya lewat Fixture BE atau fixture waktu yang mencatat jam server saat Publish. Tidak ada endpoint yang dikarang; yang diminta hanya kemampuan membaca T4.
  - Sesi login Total Control tetap valid setelah jam server maju lebih dari 24 jam pada TC-AC-PP-94 (TTL sesi uji diperpanjang oleh tim FE, atau token sesi diterbitkan ulang oleh hook sebelum langkah UI sesudah jam maju). TC tidak menyatakan apa pun tentang masa berlaku sesi (lihat Temuan untuk QA).
  - Activity Log Admin Console dapat dibaca untuk menghitung entri `Publish`.
- Baseline log: sebelum aksi Publish tiap TC, spec mencatat jumlah entri `Publish` (Object `Privacy Policy`) dengan Name `Version 4` (dan `Version 5` pada TC-AC-PP-94) di Activity Log. Entri log tidak dihapus oleh Fixture BE, sehingga asersi memakai selisih terhadap baseline.
- Suite berjalan serial (`parallel: false`): spec ini mengubah jam server (state global) dan mem-publish versi baru pada dokumen Privacy Policy tunggal platform-wide. Hook `after` memulihkan jam server dan dataset ke Riwayat A.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-94: Key idempotency melewati masa berlaku diperlakukan sebagai permintaan baru

1. Buka Admin Console > Activity Log dan catat jumlah entri `Publish`, Object `Privacy Policy`, untuk Name `Version 4` (baseline B4-94) dan untuk Name `Version 5` (baseline B5-94)
2. Buka Settings > Privacy Policy
3. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
4. Pasang intercept yang menangkap permintaan Publish (key K) tanpa mengubahnya
5. Klik di akhir konten editor lalu ketik " Expiry case."
6. Klik `[Publish New Version]` lalu klik `[Publish]` sehingga `Version 4` terbentuk dengan key K
7. Majukan jam server (fixture waktu) sebesar 24 jam 1 menit
8. Klik `[⋯]` pada baris `Version 4` → pilih `Edit`, tunggu konten termuat
9. Klik di akhir konten editor lalu ketik " Again."
10. Ganti intercept: permintaan Publish berikutnya memakai key K
11. Klik `[Publish New Version]`
12. Klik `[Publish]`
13. Verifikasi permintaan dengan key K setelah masa berlaku diperlakukan sebagai permintaan baru (tidak ada respons ulang dari permintaan sebelumnya)
14. Verifikasi toast sukses "Success, Privacy Policy has been published." tampil
15. Verifikasi tabel menampilkan `Version 5` berbadge `Active`
16. Klik teks tautan `Version 5`
17. Verifikasi konten `Version 5` berbeda dari konten `Version 4` (memuat ` Expiry case. Again.`)
18. Tutup modal View dengan `[✕]`
19. Buka Admin Console > Activity Log dan hitung entri `Publish`, Object `Privacy Policy`
20. Verifikasi jumlah entri `Publish` untuk `Version 4` bertambah tepat 1 dari B4-94
21. Verifikasi jumlah entri `Publish` untuk `Version 5` bertambah tepat 1 dari B5-94
22. Lepas intercept dan pulihkan jam server ke jam nyata

### TC-AC-PP-212: Key idempotency tepat 24 jam sejak permintaan pertama masih berlaku dan dijawab sebagai replay

23. Kembalikan dataset ke Riwayat A lewat Fixture BE
24. Buka Admin Console > Activity Log dan catat jumlah entri `Publish`, Object `Privacy Policy`, Name `Version 4` sebagai baseline B-212
25. Buka Settings > Privacy Policy
26. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`, tunggu konten termuat
27. Pasang intercept yang menangkap permintaan Publish (key K dan isi permintaan) tanpa mengubahnya
28. Klik di akhir konten editor lalu ketik " Boundary case."
29. Klik `[Publish New Version]` lalu klik `[Publish]` sehingga `Version 4` terbentuk dengan key K
30. Catat waktu tersimpan `Version 4` (T4) dari sumber waktu simpan pada Prerequisites
31. Atur jam server secara absolut ke T4 ditambah tepat 24 jam, lalu bekukan
32. Kirim ulang lewat klien HTTP permintaan Publish yang identik dengan permintaan pertama (key K, konten sama) dengan token sesi Total Control
33. Verifikasi server menjawab sukses seperti permintaan pertama (replay)
34. Verifikasi respons tidak membuat versi baru
35. Lepas intercept, pulihkan jam server ke jam nyata, lalu muat ulang Settings > Privacy Policy
36. Verifikasi tabel tetap memuat `Version 4` sebagai versi terbaru
37. Verifikasi tidak ada `Version 5` di tabel
38. Buka Admin Console > Activity Log dan hitung entri `Publish`, Object `Privacy Policy`, Name `Version 4`
39. Verifikasi jumlah entri `Publish` untuk `Version 4` bertambah tepat 1 dari B-212

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Kelas harness: d (jam server, TTL sebagai batas yang diuji), dengan intercept (b) dan klien HTTP.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah baseline dan pembacaan Activity Log di kedua blok, langkah menutup modal View di blok TC-AC-PP-94, langkah melepas intercept dan memulihkan jam server di akhir tiap blok, langkah mengembalikan dataset ke Riwayat A lewat Fixture BE di awal blok TC-AC-PP-212 (TC menetapkan dataset Riwayat A di awal tiap TC dan riwayat append-only), serta langkah mencatat T4. Langkah membuka `Version 5` dan membaca kontennya di blok TC-AC-PP-94 adalah pembacaan konten untuk Expected b.
- Ukuran spec sedikit melewati sekitar 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Dua blok TC tidak saling bergantung (dataset dikembalikan di awal blok, jam server dipulihkan di akhir blok), satu kelas (d) dan satu topik (masa berlaku key idempotency); spec tidak dipecah.
- Penyimpangan dari TC-AC-PP-94: langkah 3 TC menulis "konten ` Expiry case.` ditambah ` Again.`" sehingga spec membuka Edit pada `Version 4` (konten `Version 3` + ` Expiry case.`) dan menambah ` Again.`; permintaan kedua bukan dibuat dengan klien HTTP tetapi lewat UI dengan intercept yang menimpa key, karena Expected b menyebut toast sukses UI.
- Pembagian TC lintas spec: TC-AC-PP-91, 203, 206, 213, 214 ada di `TC-AC-PP-E2E-030`; TC-AC-PP-92, 93, 202 ada di `TC-AC-PP-E2E-031`.
- Temuan untuk QA:
  - TC-AC-PP-94 langkah 3 ("Kirim ulang permintaan Publish dengan key K") tidak menyebut sarana pengiriman (UI atau klien HTTP), sedangkan TC-AC-PP-212 menyebut klien HTTP; Expected TC-AC-PP-94 menyebut toast sukses dan badge di tabel yang hanya terlihat di UI.
  - Nama header dan cara membaca key K tidak ada di TC maupun `openapi.yaml` (NC-02 mencatat openapi belum memuat key); spec tidak menulis nama header.
  - TC-AC-PP-212 tidak menyebut apakah jam server dibekukan atau digeser; spec memakai jam absolut T4 + 24 jam (batas eksak) sesuai bagian 6 konvensi.
  - TC-AC-PP-212 (dan TC-AC-PP-94) mensyaratkan "tepat 24 jam sejak Version 4 tersimpan" tetapi tidak menyebut cara memperoleh waktu simpan dengan ketelitian detik; Published At hanya tampil sebagai tanggal (NC-11). Spec mencatat sumber waktu simpan sebagai kebutuhan tim FE di Prerequisites.
  - TC-AC-PP-94 memakai UI (Edit, Publish, tabel) setelah jam server maju lebih dari 24 jam, dan TC tidak menyatakan apakah sesi login Total Control tetap valid. Spec tidak menambah langkah login ulang karena tidak ada di TC; kelangsungan sesi dicatat sebagai kebutuhan tim FE di Prerequisites.
  - Post Condition kedua TC ("Version 4 dan Version 5 tersimpan dengan masing-masing satu record audit") sebagian punya padanan Expected (Activity Log) dan diasersi lewat Expected tersebut; sisanya tidak diasersi.

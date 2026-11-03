---
id: TC-AC-PF-E2E-070-plan-name-create-default-plan-validasi-keunikan-emoji-dan-batas-120
title: "Plan Name Create Default Plan: Validasi Kosong, Emoji, Keunikan, dan Batas 120 Karakter"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-169
  - TC-AC-PF-170
  - TC-AC-PF-171
  - TC-AC-PF-614
coverage:
  web: automated
---

# Plan Name Create Default Plan: Validasi Kosong, Emoji, Keunikan, dan Batas 120 Karakter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan S (Default SAMS: `Supply Starter` Free dan `Supply Pro` Paid; slot Paid tersisa) dan Dataset Plan A (untuk TC-AC-PF-171: SIEM dengan default plan Paid `SIEM`). `before` menyemai kedua Dataset sekaligus; Product SAMS berasal dari Dataset Plan S, Product lain dari Dataset Plan A. `SIEM` adalah nama literal Pre-setup yang hanya dibaca (A-6).
- Data Dinamis: nama 121 karakter = `Paket` + huruf `a` + `{runId}-070` dengan jumlah `a` disesuaikan agar total tepat 121 karakter termasuk suffix; nama 120 karakter = nama yang sama dikurangi satu `a` sehingga total tepat 120 karakter (R-06). Nama 120 karakter dibuat sebagai default plan Paid SAMS pada TC-AC-PF-170; dihapus fixture BE di hook `after`.
- Kemampuan teknis tambahan: menyuntikkan nilai langsung ke DOM field Plan Name (melewati filter keystroke FE) pada TC-AC-PF-614.
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-070`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-169: Validasi Plan Name Create Default Plan: kosong ditolak setelah Submit

1. Klik `+ Default Plan`
2. Pilih Product `SAMS`, pilih Pricing Type `Paid`
3. Biarkan Plan Name kosong lalu klik `[Submit]`
4. Verifikasi pesan inline `Plan name must not be empty` setelah Submit
5. Verifikasi plan tidak tersimpan: form tetap terbuka pada halaman New Default Plan tanpa toast sukses
6. Klik `[Clear Field]`

### TC-AC-PF-614: Karakter Plan Name Create Default Plan: emoji diblok saat mengetik dan ditolak server bila lolos filter input

7. Pilih Product `SAMS` dan Pricing Type `Paid`
8. Klik field Plan Name lalu ketik `😊`
9. Verifikasi emoji tidak masuk ke field Plan Name
10. Injeksi nilai `Supply 😊` langsung ke DOM field Plan Name (melewati filter keystroke FE)
11. Klik `[Submit]`
12. Verifikasi pesan inline `Plan name contains invalid characters`
13. Verifikasi plan tidak tersimpan: form tetap terbuka pada halaman New Default Plan tanpa toast sukses
14. Klik `[Clear Field]`

### TC-AC-PF-171: Keunikan Plan Name Create Default Plan di antara sesama default plan Product yang sama

15. Pilih Product `SIEM`
16. Ketik `SIEM` pada Plan Name dan tunggu 1 detik
17. Verifikasi pesan inline `Plan name already exists`
18. Ubah Plan Name menjadi `siem  ` (dua spasi di akhir) lalu tunggu 1 detik
19. Verifikasi pesan inline `Plan name already exists`
20. Klik `[Clear Field]`

### TC-AC-PF-170: Batas karakter Plan Name Create Default Plan: 120 diterima dan 121 memunculkan error langsung

21. Pilih Product `SAMS`, Pricing Type `Paid`
22. Isi Plan Name dengan nama 121 karakter
23. Verifikasi pesan `Max. 120 characters` muncul langsung
24. Verifikasi `[Submit]` diblok
25. Ubah Plan Name menjadi nama 120 karakter
26. Verifikasi tidak ada pesan error `Max. 120 characters`
27. Klik `[Submit]`
28. Verifikasi toast sukses: "Success, default plan has been created."

## Notes

- Urutan blok mengikuti bagian 3: validasi yang diblokir (TC-AC-PF-169, TC-AC-PF-614, TC-AC-PF-171) sebelum aksi sukses, dan TC-AC-PF-170 yang menyimpan plan di akhir. Karena itu TC-AC-PF-171 ditempatkan sebelum TC-AC-PF-170.
- Langkah penghubung (S-03, S-09): `[Clear Field]` di akhir blok TC mengembalikan form ke keadaan bersih sehingga TC berikutnya tidak mewarisi isi atau pesan error, dan form tidak berakhir dirty.
- Asersi "tidak ada plan baru" dan "plan tidak tersimpan" pada penolakan validasi ditulis sebagai form tetap terbuka pada halaman New Default Plan tanpa toast sukses; TC tidak memberi cara observasi lain.
- P-5 butir b: TC-AC-PF-614 memakai injeksi DOM langsung (bypass filter FE, kelas a tanpa harness eksternal dan tanpa state berat) sebagai satu-satunya TC objek-uji ringan kelas a di spec fungsional ini; pesan error ditolak server tampil di form yang sama.
- Pada TC-AC-PF-171 jeda 1 detik mengikuti Langkah TC (waktu debounce validasi keunikan), kurang dari 30 detik.
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-170 Expected a menulis "Submit diblok" tanpa menyatakan apakah tombol `[Submit]` Disabled atau klik ditolak; spec menulis `Verifikasi` `[Submit]` diblok mengikuti teks TC.
-   - TC-AC-PF-169 sampai TC-AC-PF-172 menyebut Dataset Plan S pada Pre-setup TC-AC-PF-169/170 dan Dataset Plan A pada TC-AC-PF-171, sedangkan Dataset Plan A mendefinisikan SAMS kosong dan Dataset Plan S mendefinisikan SAMS berisi plan; spec menyemai keduanya dengan SAMS dari Dataset Plan S.

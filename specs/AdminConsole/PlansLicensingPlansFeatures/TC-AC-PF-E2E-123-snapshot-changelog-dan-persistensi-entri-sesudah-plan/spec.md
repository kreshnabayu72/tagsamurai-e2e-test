---
id: TC-AC-PF-E2E-123-snapshot-changelog-dan-persistensi-entri-sesudah-plan
title: "Snapshot Changelog: Entri Tetap Terbaca Sesudah Plan Dihapus atau Akun Dihapus, Rename Dua Kali, dan Dua Edit Beruntun"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-529
  - TC-AC-PF-539
  - TC-AC-PF-540
  - TC-AC-PF-541
coverage:
  web: automated
---

# Snapshot Changelog: Entri Tetap Terbaca Sesudah Plan Dihapus atau Akun Dihapus, Rename Dua Kali, dan Dua Edit Beruntun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): `Arsip Custom Dua` (archived, tampil di sub-tab Archive sebagai anchor) dan `Growth Tier` v20 (Group count `25`, Borrowing `Full`; target aksi tulis); Dataset Log C (Pre-setup #41): Changelog Custom Principal 6 entri, termasuk entri `Delete` `Pilot Reseller` oleh `Jane S` dan entri `Create` `Growth Tier` oleh `John D`. General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Pengecualian S-06/S-12 butir A-14 dipakai (nama literal tanpa suffix dan target aksi tulis pada data Pre-setup).
- Precondition TC yang disiapkan di hook `before` lewat Fixture BE (disediakan tim FE/BE, idempoten): `Arsip Custom Satu` dengan riwayat Create, Edit, Archive, lalu Delete permanen (TC-AC-PF-529; dipulihkan di hook `after`), dan akun `Jane Smith` dihapus sehingga entri Changelog atasnya tetap tampil sebagai `Jane S` (TC-AC-PF-540; dipulihkan di hook `after`).
- State global: suite serial (`parallel: false`). Pemulihan `Growth Tier` v20 ke keadaan awal dijamin Fixture BE (idempoten): dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 33 dan 48). Efek yang tersisa: Last Modified `Growth Tier` dan entri Changelog Custom (permanen) yang dikembalikan lewat Fixture BE (Pre-setup Dinamis #4).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk riwayat plan terhapus, akun dihapus, dan pemulihan Dataset.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-529: Entri Changelog tetap terbaca sesudah plan dihapus permanen

1. Klik tab `Custom` sub-tab `Archive`
2. Verifikasi `Arsip Custom Dua` tampil di sub-tab Archive (anchor)
3. Verifikasi `Arsip Custom Satu` tidak ada di sub-tab Archive
4. Klik ikon Changelog pada toolbar tab Custom
5. Ketik Search `Arsip Custom Satu`, tekan Enter
6. Verifikasi Entri Action `Create`, `Edit`, `Archive`, dan `Delete` untuk `Arsip Custom Satu` tetap terbaca
7. Verifikasi Kolom Plan Name pada keempat entri memakai nama tersimpan `Arsip Custom Satu` meskipun plan sudah tidak ada di list
8. Klik `(←)` pada kotak Search

### TC-AC-PF-540: Modified By tetap nama saat aksi walau akun aktor dihapus

9. Ketik Search `Pilot Reseller`, tekan Enter
10. Verifikasi Kolom Modified By entri `Delete` `Pilot Reseller` tampil `Jane S` (snapshot, bukan `—`)
11. Hover `Jane S`
12. Verifikasi Tooltip `Jane Smith`
13. Klik `(←)` pada kotak Search
14. Tutup modal Changelog

### TC-AC-PF-539: Snapshot Immutability, rename dua kali

15. Klik tab `Custom` sub-tab `Active`
16. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
17. Ganti Plan Name menjadi `Tier Satu`
18. Klik `[Save]`
19. Tunggu aksi selesai (Plan Detail `Tier Satu` terbuka)
20. Kembali ke Plans List tab Custom sub-tab Active
21. Buka Overlay Row Action `Tier Satu`, lalu klik `Edit`
22. Ganti Plan Name menjadi `Tier Dua`
23. Klik `[Save]`
24. Tunggu aksi selesai (Plan Detail `Tier Dua` terbuka)
25. Kembali ke Plans List tab Custom sub-tab Active
26. Klik ikon Changelog pada toolbar tab Custom
27. Ketik Search `Tier`, tekan Enter
28. Verifikasi Entri rename pertama tetap: Plan Name `Tier Satu`, Field `Plan Name`, Old Value `Growth Tier`, New Value `Tier Satu`
29. Verifikasi Entri rename kedua: Plan Name `Tier Dua`, Field `Plan Name`, Old Value `Tier Satu`, New Value `Tier Dua`
30. Verifikasi Entri `Create` lama tetap menampilkan Plan Name `Growth Tier` sebagaimana saat dicatat
31. Klik `(←)` pada kotak Search
32. Tutup modal Changelog
33. Pulihkan Dataset Pre-setup (`Growth Tier` v20) lewat Fixture BE

### TC-AC-PF-541: Dua perubahan beruntun pada field berbeda

34. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
35. Ubah Group count `25` menjadi `3`
36. Klik `[Save]`
37. Tunggu aksi selesai (Plan Detail `Growth Tier` terbuka)
38. Kembali ke Plans List tab Custom sub-tab Active
39. Buka Overlay Row Action `Growth Tier`, lalu klik `Edit`
40. Ubah Borrowing `Full` menjadi `Basic`
41. Klik `[Save]`
42. Verifikasi Judul Plan Detail `Growth Tier – v22`
43. Kembali ke Plans List tab Custom sub-tab Active
44. Klik ikon Changelog pada toolbar tab Custom
45. Verifikasi Dua entri terpisah (satu per Edit) dengan Field `Group count` dan Field `Borrowing`
46. Verifikasi Entri pertama (Field `Group count`, Old Value `25`, New Value `3`) tidak berubah setelah Edit kedua
47. Tutup modal Changelog
48. Pulihkan Dataset Pre-setup (`Growth Tier` v20) lewat Fixture BE

## Notes

- Urutan TC di dalam spec: TC-AC-PF-529 dan TC-AC-PF-540 (pembacaan saja) di awal, lalu TC-AC-PF-539 dan TC-AC-PF-541 (aksi tulis), mengikuti urutan bagian 3 (S-10).
- Langkah penghubung (S-03): buka tab dan sub-tab sebagai precondition TC, Search `Arsip Custom Satu`, `Pilot Reseller`, dan `Tier` untuk menemukan baris target di modal Changelog (R-16; langkah 5, 9, 27) lalu `(←)` untuk membersihkannya, "Tunggu aksi selesai" sebelum pindah surface (bagian 8b butir 8), kembali ke Plans List, tutup modal Changelog, dan pemulihan Dataset lewat Fixture BE (langkah 33 dan 48). Langkah 2 dan 3 membuktikan `Arsip Custom Satu` tidak ada di list dengan anchor `Arsip Custom Dua` (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-AC-PF-520 sampai TC-AC-PF-528 dan TC-AC-PF-530 ada di spec 121 dan spec 122; TC-AC-PF-531 ada di spec 128.
- Alasan melewati sekitar 35 langkah (48 langkah): keempat TC membaca atau menulis Changelog Custom pada satu dataset dan satu kelas harness (fungsional). Langkah baca-log (buka Changelog, Search, `Verifikasi` kolom log, tutup modal: langkah 4 sampai 14, 26 sampai 32, dan 43 sampai 47) mengikuti pola buka surface lalu Verifikasi yang tidak dihitung pada ambang menurut bagian 3 prinsip 13; tanpa blok itu spec ini 25 langkah.
- Temuan untuk QA:
  - TC-AC-PF-529 dan TC-AC-PF-540 bergantung pada data hasil Fixture BE (plan terhapus dan akun dihapus) yang tidak ada di Tabel Pre-setup; spec menuliskannya sebagai kemampuan "disediakan tim FE/BE" tanpa endpoint karangan.
  - TC-AC-PF-540 tidak menyebut baris entri `Jane S` yang diamati; spec memakai entri `Delete` `Pilot Reseller` (Dataset Log C, oleh `Jane S`) dan Search untuk menemukannya.
  - TC-AC-PF-529 Expected "meskipun plan sudah tidak ada di list" tidak menyebut sub-tab; spec memeriksa sub-tab Archive, tempat plan itu berada sebelum dihapus.
  - TC-AC-PF-539 butir c ("Entri Create lama") tidak menyebut baris Create yang diamati; spec memakai entri `Create` `Growth Tier` (Dataset Log C).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01): TC-AC-PF-540 ("Entri tidak berubah") dan TC-AC-PF-541 ("dua snapshot versi" selain `v22` pada langkah 42).

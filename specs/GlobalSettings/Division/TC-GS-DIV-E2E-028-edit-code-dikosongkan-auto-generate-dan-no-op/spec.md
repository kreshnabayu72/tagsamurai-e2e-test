---
id: TC-GS-DIV-E2E-028-edit-code-dikosongkan-auto-generate-dan-no-op
title: "Edit Division: Code Dikosongkan, Auto-Generate, dan Save Tanpa Perubahan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-99
  - TC-GS-DIV-288
  - TC-GS-DIV-100
  - TC-GS-DIV-98
coverage:
  web: automated
---

# Edit Division: Code Dikosongkan, Auto-Generate, dan Save Tanpa Perubahan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor di hook `before` spec ini (seedSession, kredensial dari env var), lalu sesi dipakai sepanjang spec. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup (TC-GS-DIV-99 menguji baris Pre-setup secara eksplisit; pengecualian S-06 `[KEPUTUSAN 2026-10-21]`: baris Pre-setup in-use menjadi target aksi no-op): Division `Human Resources` (Code `HR`, in-use Login User aktif). Edit pada langkah 2 sampai 4 adalah no-op sehingga baris ini tidak berubah, termasuk Last Updated. Fixture belum ada; tim FE menyiapkan `fixtures/division.json` untuk identitas data ini.
- Data dengan nama dan Code literal TC tanpa suffix per run, karena asersi bergantung pada hasil auto-generate Code (`CS` dari `Customer Service`; `IT` dari `Information Technology`) (S-12):
  - `Customer Service` dengan Code `CSV` (TC-GS-DIV-98) diubah Code-nya menjadi `CS`. Division bernama itu juga merupakan anggota Population D-02; hook `before` menghapus lewat API Division bernama `Customer Service` bila sudah ada, lalu men-seed milik spec ini (pengecualian S-12 `[KEPUTUSAN 2026-10-21]` untuk Name literal penentu hasil auto-generate Code: seeding idempotent, cleanup milik spec, suite serial). Hook `after` menghapusnya lagi.
  - `Information Technology` dengan Code `IT` (TC-GS-DIV-288) tidak berubah (Edit adalah no-op). Hook `before` men-seed idempotent (dilewati bila sudah ada, misalnya dari Population D-02) dan hook `after` hanya menghapus bila dibuat spec ini.
- Data dinamis bersuffix: `Noop {runId}-028` dengan Code `E28A` (TC-GS-DIV-100; pengganti `Accounting` pada TC sumber), seeding Division lewat API di hook `before`, dihapus di hook `after`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API `Customer Service`, `Information Technology` (hanya bila dibuat spec ini), dan `Noop {runId}-028` bila masih ada. Hook `beforeEach`: tutup dialog atau modal yang terbuka lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: mengetik 3 spasi pada Code; membaca Modal Changelog (jumlah total entri sebagai baseline, kolom Division Name, Field, Old Value, New Value); seeding dan penghapusan Division lewat API.
- Layar awal `Global Settings > User > Division` dibuka di hook `beforeEach` (konvensi bagian 4).
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: Division `Customer Service` Population D-02 dihapus dan diganti Division milik spec (dijelaskan di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-DIV-99: Edit dengan Code dikosongkan yang hasil generate identik dengan Code sendiri tidak berubah

1. Ketik Search `Human Resources`, tekan Enter
2. Buka row action baris `Human Resources` lalu klik `Edit`
3. Kosongkan Code
4. Klik `[Save]`
5. Verifikasi tidak ada error pada Code (kandidat `HR` hanya bentrok dengan record itu sendiri sehingga tidak dihitung bentrok)
6. Verifikasi toast netral: `No changes to save.`
7. Verifikasi modal Edit menutup
8. Verifikasi Code baris `Human Resources` tetap `HR`

### TC-GS-DIV-288: Edit dengan Code berisi spasi saja dianggap kosong dan di-generate otomatis

9. Ganti isi kotak search dengan `Information Technology`, tekan Enter
10. Buka row action baris `Information Technology` lalu klik `Edit`
11. Ganti isi Code dengan 3 spasi
12. Verifikasi tidak ada error pada Code
13. Klik `[Save]`
14. Verifikasi tidak ada error pada Code setelah `[Save]` (kandidat `IT` hanya bentrok dengan record itu sendiri sehingga tidak dihitung bentrok)
15. Verifikasi toast netral: `No changes to save.`
16. Verifikasi modal Edit menutup
17. Verifikasi Code baris `Information Technology` tetap `IT`

### TC-GS-DIV-100: Save Edit tanpa perubahan data menutup modal dengan toast netral

18. Ganti isi kotak search dengan `Noop {runId}-028`, tekan Enter
19. Buka row action baris `Noop {runId}-028` lalu klik `Edit`
20. Klik `[Save]` tanpa mengubah field apa pun
21. Verifikasi toast netral (info): `No changes to save.`
22. Verifikasi toast itu bukan toast sukses
23. Verifikasi modal Edit menutup otomatis
24. Verifikasi tidak ada dialog Unsaved Changes
25. Verifikasi tidak ada pesan error

### TC-GS-DIV-98: Edit dengan Code dikosongkan di-generate otomatis dan dicatat bila berbeda

26. Buka Modal Changelog
27. Catat jumlah total entri Changelog sebagai baseline (penanda sebelum aksi pada langkah 32)
28. Tutup Modal Changelog
29. Ganti isi kotak search dengan `Customer Service`, tekan Enter
30. Buka row action baris `Customer Service` lalu klik `Edit`
31. Kosongkan Code
32. Klik `[Save]`
33. Verifikasi toast sukses: `Success, division has been updated.`
34. Verifikasi tabel menampilkan Code `CS` hasil auto-generate pada baris `Customer Service`
35. Buka Modal Changelog
36. Verifikasi jumlah total entri Changelog bertambah tepat 1 dari baseline langkah 27
37. Verifikasi entri baru Changelog untuk Division `Customer Service` dengan Field `Code`, Old Value `CSV`, dan New Value `CS`
38. Tutup Modal Changelog

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-99, 288, 100, 98). Mode: FE+BE. Kelas harness: aksi sukses (Edit tanpa perubahan dan Edit dengan Code hasil generate).
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC berbeda dari urutan nomor TC sumber: tiga kasus no-op (TC-99, TC-288, TC-100) lebih dulu karena tidak mengubah data, dan TC-GS-DIV-98 terakhir karena mengubah Code dan membuka Changelog.
- Pembagian TC lintas spec: asersi "tidak ada entri log baru" TC-GS-DIV-99 butir d, TC-GS-DIV-288 butir d, dan TC-GS-DIV-100 butir d (Changelog, Activity Log, dan Tab System Log aktor) berada di spec `TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use`, yang memuat aksi nyata dan baseline sendiri untuk ketiga TC itu. Spec ini memuat Expected lain dari ketiganya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 9, 18, dan 29 (mencari target Edit lewat Search; Search diganti nilai baru pada pencarian berikutnya); langkah 26 sampai 28 (membuka Modal Changelog, mencatat jumlah total entri sebagai baseline sebelum Save, menutup Modal); langkah 35 dan 38 (membuka dan menutup Modal Changelog).
- Langkah 22 memecah klausa "bukan toast sukses" dari Expected a TC-GS-DIV-100.
- Temuan untuk QA:
  - TC-GS-DIV-98 memakai Name `Customer Service` yang juga ada di Population D-02 (TC-GS-DIV-30) dengan Code `CSV`; Edit mengubah Code menjadi `CS` sehingga baris Population bersama berubah. Spec menghapus baris Population itu dan men-seed milik sendiri; keputusan ini perlu disetujui tim FE karena spec lain yang memakai Population D-02 men-seed ulang idempotent.
  - Post Condition TC-GS-DIV-99, 288, dan 100 ("Code tetap", "Last Updated tidak berubah") hanya sebagian punya padanan di Expected; "Last Updated tidak berubah" (TC-GS-DIV-100) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-GS-DIV-98 butir c ("Changelog mencatat perubahan Code CSV menjadi CS") tidak menyebut nilai kolom Division Name dan Field di entri; spec mengasersi Division Name, Field `Code`, Old Value, dan New Value.
- Spec melewati sekitar 35 langkah (38 langkah) karena memuat empat TC Edit Code dikosongkan dan tanpa perubahan pada satu fitur yang sama; seluruhnya satu kelas harness (aksi sukses), tiap blok memakai Division dan form sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.

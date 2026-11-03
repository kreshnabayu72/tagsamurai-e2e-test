---
id: TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel
title: "Changelog: Screening, State, dan Format Sel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-398
  - TC-AC-CS-399
  - TC-AC-CS-401
  - TC-AC-CS-403
  - TC-AC-CS-404
  - TC-AC-CS-405
coverage:
  web: automated
---

# Changelog: Screening, State, dan Format Sel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- General Settings Principal PT ABC: Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00`; tanggal acuan uji `19/08/26` (Pre-setup #28).
- Pada blok TC-AC-CS-405, jam server dan jam browser sinkron dan tidak digeser; tidak ada state global yang diubah spec ini.

## Test Steps

### TC-AC-CS-398: Screening modal Changelog: Client Subscription

1. Klik ikon Changelog di toolbar
2. Verifikasi judul "Changelog: Client Subscription" dan tombol silang `[✕]` tampil di header
3. Verifikasi modal tanpa Breadcrumb
4. Verifikasi Table Tools: Search, Filter, Download tampil
5. Verifikasi kolom: `Date` (sortable, default sort Newest First), `Action` (sortable), `Client — Product` (sortable), `Field` (sortable), `Old Value` (sortable), `New Value` (sortable), `Modified By` (sortable)
6. Verifikasi tabel read-only tanpa row action
7. Verifikasi tabel menampilkan sedikitnya satu entri
8. Verifikasi entri terurut Date Newest First
9. Verifikasi kolom Actions kosong dengan `⋯` sebagai trigger Column Visibility pada header
10. Verifikasi Pagination default 10 baris per halaman

### TC-AC-CS-401: Empty filtered Modal Changelog

11. Ketik Search `zzzzqqq`, tekan Enter
12. Verifikasi empty state menampilkan Illustration, Title "No results found", dan Description "Try adjusting your search or filter."
13. Verifikasi empty state ini berbeda dari empty state S-06
14. Klik `(←)` pada kotak Search

### TC-AC-CS-403: Format sel Client — Product serta Old Value dan New Value kosong

15. Ketik Search `PT Sejahtera`, tekan Enter
16. Verifikasi entri Activate Trial menampilkan Client Name saja (`PT Sejahtera`) tanpa Product
17. Verifikasi Old Value entri Activate ditampilkan `—`
18. Ganti isi kotak search dengan `Percetakan Mega`, tekan Enter
19. Verifikasi entri Add Subscription menampilkan `Percetakan Mega — FAMS` sebagai plain text, bukan link
20. Verifikasi Old Value entri Add Subscription ditampilkan `—`
21. Ganti isi kotak search dengan `Renew (request, submit)`, tekan Enter
22. Verifikasi Old Value entri Renew request ditampilkan `—`
23. Ganti isi kotak search dengan `Schedule Renewal`, tekan Enter
24. Verifikasi Old Value entri Schedule Renewal ditampilkan `—`
25. Ganti isi kotak search dengan `Resubmit`, tekan Enter
26. Verifikasi Old Value entri Resubmit ditampilkan `—`
27. Klik `(←)` pada kotak Search
28. Verifikasi tabel menampilkan sedikitnya satu entri
29. Verifikasi New Value tidak pernah kosong pada setiap entri yang tampil

### TC-AC-CS-404: Modified By berupa plain text dengan tooltip nama lengkap dan System untuk job

30. Ketik Search `Fajar`, tekan Enter, lalu arahkan kursor ke Modified By `Fajar N`
31. Verifikasi Modified By berformat `[First Name] [Initial]` plain text, bukan badge
32. Verifikasi hover menampilkan nama lengkap user (`Fajar Nugroho`)
33. Ganti isi kotak search dengan `Scheduled Flip`, tekan Enter
34. Verifikasi entri hasil Scheduled Flip menampilkan Modified By `System`
35. Ganti isi kotak search dengan `Timeout Auto-Cancel`, tekan Enter
36. Verifikasi entri hasil Timeout Auto-Cancel menampilkan Modified By `System`
37. Klik `(←)` pada kotak Search

### TC-AC-CS-405: Kolom Date mengikuti format General Settings

38. Amati kolom Date entri teratas pada halaman 1
39. Verifikasi tanggal dan jam entri `19/08/26 11:50` tampil sesuai Date Format `dd/MM/yy` dan Time Format 24-hour pada zona Asia/Jakarta

### TC-AC-CS-399: Modal Changelog ditutup lewat silang atau Esc dan tidak lewat klik backdrop

40. Klik area gelap di luar modal
41. Verifikasi klik backdrop tidak menutup modal
42. Verifikasi tidak ada tombol teks Close di footer
43. Klik `[✕]`
44. Verifikasi modal Changelog tertutup oleh `[✕]`
45. Klik ikon Changelog di toolbar lalu tekan `Esc`
46. Verifikasi modal Changelog tertutup oleh `Esc`

## Notes

- Spec ini melewati sekitar 35 langkah. Alasannya: seluruh blok satu topik (screening dan format tampilan Modal Changelog) pada seed #84 yang sama, baca-saja, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca-log berpola (buka modal, cari entri, `Verifikasi` kolom entri) tidak dihitung pada ambang sekitar 35 langkah (bagian 3, Smell).
- Urutan blok mengikuti bagian 3: screening di awal, blok TC-AC-CS-399 (menutup modal) di akhir.
- Langkah penghubung (S-03): Search untuk menemukan entri target pada blok TC-AC-CS-403 dan TC-AC-CS-404 (R-16), langkah `(←)` yang mengosongkan Search sesudah tiap blok, dan klik ikon Changelog untuk membuka modal kembali pada blok TC-AC-CS-399.
- Asersi urutan (Date Newest First, langkah 8) dan asersi universal ("New Value tidak pernah kosong") didahului `Verifikasi` sedikitnya satu entri pada permukaan yang sama (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-CS-401 Expected b ("Berbeda dari empty state S-06") merujuk S-06 tanpa definisi di baris TC; spec menuliskannya apa adanya.
  - TC-AC-CS-403 tidak menyebut cara menemukan entri `Activate` Trial `PT Sejahtera`, `Add Subscription`, `Renew (request, submit)`, `Schedule Renewal`, dan `Resubmit`; spec memakai Search (langkah penghubung).
  - TC-AC-CS-405 menyebut entri `19/08/26 11:50` tanpa menyebut posisinya; spec mengamati entri teratas halaman 1 berdasarkan default sort Date Newest First pada seed #84 yang dipulihkan baseline.
  - TC-AC-CS-404 butir Langkah Uji ke-3 ("Amati entri hasil scheduled flip") tidak menyebut entri yang diamati; spec mencari lewat Search `Scheduled Flip` dan `Timeout Auto-Cancel`.

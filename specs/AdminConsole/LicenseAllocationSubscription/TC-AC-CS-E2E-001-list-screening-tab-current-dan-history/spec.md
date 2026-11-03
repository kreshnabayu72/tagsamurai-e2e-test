---
id: TC-AC-CS-E2E-001-list-screening-tab-current-dan-history
title: "List: Screening Tab Current dan History"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-1
  - TC-AC-CS-2
  - TC-AC-CS-3
  - TC-AC-CS-4
  - TC-AC-CS-7
coverage:
  web: automated
---

# List: Screening Tab Current dan History

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`, Total Control, Principal PT ABC; Pre-setup #1), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #82 (120 baris term di tab Current dan 60 baris di tab History untuk Client campuran, Plan Owner PT Maju Bersama dan CV Karya Mandiri) bersifat baca-saja; spec tidak menulis data.
- Kemampuan teknis: `Spectra.intercept()` parsial untuk menunda respons endpoint data List di atas backend nyata; endpoint tidak disebut di TC, PRD, atau LLD (S-13) sehingga nama endpoint ditentukan tim FE. Intercept dilepas segera setelah asersi state loading (S-09).

## Test Steps

### TC-AC-CS-1: Screening halaman List Subscriptions tab Current

1. Klik menu `Allocation > Client Subscription` dari sidebar
2. Susuri halaman dari atas ke bawah dan dari kiri ke kanan tanpa mengklik elemen apa pun
3. Verifikasi Breadcrumb `Allocation > Client Subscription` terdiri atas dua segmen dan tidak ada segmen yang bisa diklik
4. Verifikasi tidak ada Page Title terpisah di bawah Breadcrumb
5. Verifikasi tombol `[?]` (Show guide) tepat di sebelah kanan Breadcrumb
6. Verifikasi tab `Current` (aktif) | `History`
7. Verifikasi Table Tools: `Search | Filter | Download | Changelog | [+ Subscription] | [+ Activate Trial]`
8. Verifikasi kolom: `Subscription ID (sortable) | Client (sortable, default sort) | Product (sortable) | Plan (sortable) | Status (sortable) | Start Date (sortable) | End Date (sortable) | Plan Owner (sortable) | Column Visibility (⋯) (unsortable, header klik = buka overlay Column Visibility, body per baris = row action menu)`
9. Verifikasi kolom Grace End tidak tampil secara default (Curated)
10. Verifikasi sedikitnya satu baris tampil di tab `Current`
11. Verifikasi baris tab `Current` terurut Client A-Z, dengan baris Client yang sama terurut ID terbaru di atas
12. Verifikasi Pagination default 10 baris per halaman

### TC-AC-CS-2: Screening halaman List Subscriptions tab History

13. Klik tab `History`
14. Susuri tabel dan toolbar dari atas ke bawah tanpa mengklik elemen lain
15. Verifikasi Breadcrumb `Allocation > Client Subscription` tidak berubah
16. Verifikasi tab `Current` | `History` (aktif)
17. Verifikasi Table Tools `Search | Filter | Download` tampil
18. Verifikasi ikon Changelog, `[+ Subscription]`, dan `[+ Activate Trial]` tidak dirender di tab `History` (ACCS-LOGIC-09e)
19. Verifikasi kolom sama dengan tab Current: `Subscription ID (sortable) | Client (sortable, default sort) | Product (sortable) | Plan (sortable) | Status (sortable) | Start Date (sortable) | End Date (sortable) | Plan Owner (sortable) | Column Visibility (⋯) (unsortable, header klik = buka overlay Column Visibility, body per baris = row action menu)`
20. Verifikasi sedikitnya satu baris tampil di tab `History`
21. Verifikasi hanya baris berstatus Renewed, Rejected, Canceled, Archive, Purge, Deleted, serta baris Trial Converted, Rejected, Canceled yang tampil
22. Verifikasi baris terurut ID terbaru di atas (Created At descending)
23. Verifikasi Pagination default 10 baris per halaman, kembali ke halaman 1

### TC-AC-CS-3: Tab Current aktif saat halaman pertama kali dibuka

24. Klik menu `Allocation > Client Subscription` di sidebar
25. Verifikasi tab `Current` aktif secara default dan tab `History` tidak aktif
26. Verifikasi sedikitnya satu baris tampil di tab `Current`
27. Verifikasi tabel hanya memuat baris berstatus Waiting for Approval, Pending, Active, Expired, Grace, serta baris Trial Waiting for Approval, Active, Expired

### TC-AC-CS-4: State loading List saat data diambil

28. Tunda respons endpoint data List melalui intercept jaringan selama beberapa detik
29. Klik menu `Allocation > Client Subscription`
30. Verifikasi tabel menampilkan komponen loading selama respons tertunda
31. Verifikasi tabel bukan empty state dan bukan error selama respons tertunda
32. Lepas tahanan respons endpoint data List
33. Verifikasi loading hilang setelah respons diterima
34. Verifikasi baris data tampil

### TC-AC-CS-7: Empty state hasil pencarian tanpa kecocokan di tab Current

35. Ketik Search `zzzzqqq`, tekan Enter
36. Verifikasi Illustration tampil
37. Verifikasi Title "No results found"
38. Verifikasi Description "Try adjusting your search or filter."
39. Verifikasi Title bukan "No current subscriptions"
40. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah menunda dan melepas tahanan respons pada TC-AC-CS-4 (kebutuhan intercept ada di Prerequisites), langkah `Klik menu Allocation > Client Subscription` yang mengembalikan tab `Current` sebelum TC-AC-CS-3 dan TC-AC-CS-4, dan `Klik (←)` pada kotak Search di akhir spec.
- Verifikasi `sedikitnya satu baris tampil` pada TC-AC-CS-1, TC-AC-CS-2 dan TC-AC-CS-3 adalah pembanding generik untuk asersi universal terurut (TC-AC-CS-1) dan "hanya baris berstatus ..." (bagian 8b butir 2); TC tidak menulisnya.
- Spec ini 40 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (screening List Subscriptions) pada dataset baca-saja yang sama (kelas e, Pre-setup #82) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Dua blok screening kolom dan toolbar berisi banyak klausa Expected yang wajib dipecah per klausa (S-01).
- Temuan untuk QA:
  - TC-AC-CS-4 menyebut "endpoint data List" tanpa nama endpoint dan tanpa sumber (PRD, LLD) yang mendaftarkannya; spec memakai intercept parsial dan nama endpoint ditentukan tim FE.
  - TC-AC-CS-7 Expected d merujuk "S-02" tanpa menjelaskan isi rujukan; spec menafsirkannya sebagai Title empty state tab Current kosong ("No current subscriptions") yang berbeda dari empty state hasil pencarian.

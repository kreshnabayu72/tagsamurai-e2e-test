---
id: TC-AC-CS-E2E-053-activate-trial-form-dirty-dan-backdrop
title: "Activate Trial: Form Dirty dan Backdrop"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-207
  - TC-AC-CS-208
  - TC-AC-CS-542
  - TC-AC-CS-558
  - TC-AC-CS-574
coverage:
  web: automated
---

# Activate Trial: Form Dirty dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup: Client `Client Tanpa Subscription` (binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial) (#48), hanya dipilih di form dan tidak pernah disubmit.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah term dan trial milik Client `Client Tanpa Subscription` lewat BE; baseline dicatat di hook `before` (0 term, 0 trial sesuai Pre-setup #48).
- Form Activate Trial dibuka sekali per kasus yang berbeda keadaan awalnya dan setiap pembukaan ditutup sebelum kasus berikutnya (S-10).

## Test Steps

### TC-AC-CS-574: Nilai dikembalikan identik dengan nilai awal dianggap clean saat ditutup

1. Klik `[+ Activate Trial]`; Trial Duration bernilai default `30`
2. Ubah Trial Duration menjadi `45` lalu kembalikan ke `30`
3. Klik `[✕]`
4. Verifikasi form dianggap clean karena nilai identik dengan nilai awal
5. Verifikasi dialog Unsaved Changes tidak muncul dan modal tertutup

### TC-AC-CS-558: Klik backdrop tidak menutup form Activate Trial walau dirty

6. Klik `[+ Activate Trial]`
7. Pilih Client `Client Tanpa Subscription`
8. Klik area gelap di luar modal
9. Verifikasi modal tetap terbuka dengan input dipertahankan
10. Verifikasi dialog Unsaved Changes tidak muncul

### TC-AC-CS-542: Pilihan Cancel pada dialog Unsaved Changes Activate Trial mempertahankan form

11. Pilih Product `FAMS`
12. Tekan `Esc`; dialog Unsaved Changes muncul
13. Klik `[Cancel]`
14. Verifikasi dialog tertutup dan modal Activate Trial tetap terbuka
15. Verifikasi nilai Client dan Product dipertahankan
16. Verifikasi jumlah trial dan term Client `Client Tanpa Subscription` yang dibaca lewat BE tetap sama dengan baseline (tidak ada trial dibuat)

### TC-AC-CS-207: Clear Field mengosongkan seluruh field Activate Trial

17. Pilih Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
18. Klik `[Clear Field]`
19. Verifikasi seluruh field kembali kosong atau default
20. Verifikasi error inline hilang
21. Verifikasi modal tetap terbuka tanpa dialog konfirmasi

### TC-AC-CS-208: Menutup form Activate Trial yang terisi memunculkan Unsaved Changes

22. Pilih Client `Client Tanpa Subscription`
23. Klik `[✕]`; dialog muncul
24. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
25. Klik `[Leave]`
26. Verifikasi dialog dan modal Activate Trial tertutup
27. Klik `[+ Activate Trial]`, lalu klik `[✕]` pada form bersih
28. Verifikasi modal tertutup tanpa dialog Unsaved Changes

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): kasus dirty dan Cancel dirangkai pada satu form (TC-AC-CS-558, 542, 207) dan kasus yang berakhir dengan `[Leave]` (TC-AC-CS-208) paling akhir; TC-AC-CS-574 paling awal karena membuka dan menutup form sendiri.
- TC-AC-CS-542 menambah pilihan Product `FAMS` pada form TC-AC-CS-558 yang sudah memilih Client `Client Tanpa Subscription`, sesuai langkah 2 TC itu (Client dan Product).
- TC-AC-CS-207 Expected b ("Error inline hilang") tidak didahului error di Langkah Uji TC; spec mengasersi tidak ada error inline setelah `[Clear Field]` (Temuan untuk QA).
- TC-AC-CS-542 Expected d ("tidak ada trial dibuat") tidak punya permukaan UI yang teramati selama form terbuka; spec membacanya lewat kemampuan BE dengan baseline (Prerequisites).
- Temuan untuk QA: TC-AC-CS-208 Expected b memuat dua klausa pada dua keadaan (setelah `[Leave]` dan form bersih); spec menambah langkah membuka form bersih untuk mengamati klausa kedua, sesuai bunyi Expected.

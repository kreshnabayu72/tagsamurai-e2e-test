---
id: TC-AC-PF-E2E-118-global-settings-auto-focus-enter-dan-unsaved-changes-sesudah-save
title: "Global Settings: Auto-Focus, Enter Tidak Men-Submit, dan Unsaved Changes Sesudah Save atau Pengembalian Nilai"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-735
  - TC-AC-PF-762
  - TC-AC-PF-763
coverage:
  web: automated
---

# Global Settings: Auto-Focus, Enter Tidak Men-Submit, dan Unsaved Changes Sesudah Save atau Pengembalian Nilai

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`; Pre-setup #1; Global Role Manage plans & licensing Create, Read, Update, Delete; Group Role Manage active client CRUD pada semua group), password dari `Spectra.env.AC_TC_PASSWORD`. Tidak ada ganti akun di tengah spec.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active).
- Data: Global FAMS Settings tersimpan `Max custom fields per asset name` = `5` dan `Max depreciation methods (Multi Depreciation tier)` = `2` (precondition TC; Tabel Pre-setup tidak memuat baris bernomor untuk data ini, lihat Temuan untuk QA).
- State global: suite serial (`parallel: false`). Global FAMS Settings adalah singleton (S-06, pengecualian 2026-10-30): nilai `5` dan `2` dipulihkan lewat Fixture BE (idempoten, disediakan tim FE/BE) di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (langkah 20). Efek yang tersisa: Save pada langkah 11 menambah entri Changelog Global Settings, System Log, dan Activity Log yang bersifat permanen (tidak dapat dihapus lewat UI).
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca nilai tersimpan Global FAMS Settings untuk asersi "tidak ada perubahan data".
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Sesi API aktor, klien HTTP, dan Fixture BE disediakan tim FE/BE sebagaimana dinyatakan di `suite.md`; endpoint tidak ditulis karena tidak ada di TC, PRD, atau LLD.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.

## Test Steps

### TC-AC-PF-735: Input pertama ter-focus dan Enter tidak men-submit

1. Klik tab `Global Settings`
2. Verifikasi Fokus langsung berada di field `Max custom fields per asset name`
3. Ubah `Max custom fields per asset name` menjadi `9`
4. Tekan Enter saat fokus berada di field `Max custom fields per asset name`
5. Verifikasi Tidak ada toast
6. Verifikasi Nilai tersimpan `Max custom fields per asset name` tetap `5` (tidak ada perubahan data)
7. Verifikasi Form tetap terbuka
8. Verifikasi Input `Max custom fields per asset name` dipertahankan (`9`)
9. Kembalikan `Max custom fields per asset name` ke nilai tersimpan `5`

### TC-AC-PF-762: Sesudah Save sukses tidak ada dialog Unsaved Changes

10. Ubah `Max custom fields per asset name` menjadi `9`
11. Klik `[Save]`
12. Verifikasi Toast sukses: "Success, global FAMS settings has been saved."
13. Klik tab `Default`
14. Verifikasi Halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung
15. Verifikasi Tidak ada dialog `Unsaved Changes`
16. Klik tab `Global Settings`
17. Klik segmen `Plans & Features` pada breadcrumb
18. Verifikasi Halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung
19. Verifikasi Tidak ada dialog `Unsaved Changes`
20. Pulihkan Global FAMS Settings ke `5` dan `2` lewat Fixture BE

### TC-AC-PF-763: Nilai dikembalikan identik, klik breadcrumb tanpa dialog

21. Klik tab `Global Settings`
22. Ubah `Max custom fields per asset name` menjadi `9`, lalu kembalikan menjadi `5`
23. Klik segmen `Plans & Features` pada breadcrumb
24. Verifikasi Halaman Plans & Licensing > Plans & Features > Default > Active tampil langsung
25. Verifikasi Tidak ada dialog `Unsaved Changes`

## Notes

- Langkah penghubung (S-03): klik tab `Global Settings` sebagai precondition TC-AC-PF-735 dan TC-AC-PF-763 (langkah 1 dan 21), klik tab `Global Settings` sebelum klik breadcrumb (langkah 16), pengembalian field ke nilai tersimpan (langkah 9), dan pemulihan Global FAMS Settings lewat Fixture BE (langkah 20; form sudah bersih sehingga tidak perlu muat ulang).
- Asersi "tidak ada toast" pada langkah 5 diletakkan segera setelah Enter (bagian 8b butir 11); langkah 2 diasersi sebelum langkah berikut yang mengubah fokus (bagian 8b butir 5).
- Pembagian TC lintas spec: TC-AC-PF-667, TC-AC-PF-674, TC-AC-PF-740, dan TC-AC-PF-745 ada di spec 117.
- Temuan untuk QA:
  - Tabel Pre-setup TC tidak memuat baris bernomor untuk nilai awal Global FAMS Settings (`5` dan `2`); nilai itu hanya tertulis di precondition tiap TC. Spec memakai S-06 pengecualian 2026-10-30 (singleton, pemulihan lewat Fixture BE).
  - Post Condition TC-AC-PF-762 ("Max custom fields per asset name bernilai 9") tanpa langkah observasi tidak diasersi (S-01).
  - TC-AC-PF-735 Expected butir b ("tidak ada perubahan data") tidak menyatakan cara membaca data; spec memakai kemampuan baca nilai tersimpan yang disediakan tim FE/BE tanpa endpoint karangan.

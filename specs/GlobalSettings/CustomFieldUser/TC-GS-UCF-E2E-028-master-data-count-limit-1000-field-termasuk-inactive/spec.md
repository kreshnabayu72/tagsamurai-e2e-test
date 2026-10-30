---
id: TC-GS-UCF-E2E-028-master-data-count-limit-1000-field-termasuk-inactive
title: "Master Data Count Limit: 1.000 Field Memuat Field Inactive Tetap Menampilkan Dialog Limit Reached"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-454
coverage:
  web: automated
---

# Master Data Count Limit: 1.000 Field Memuat Field Inactive Tetap Menampilkan Dialog Limit Reached

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`): volume 1.000 Custom Field entitas Client Limit dan status `Lim 500` diatur backend dan dipulihkan setelah spec.
- Akun aktor (login di hook `before`; password hanya lewat env var): Total Control Client Limit (Wulan Sari) `totalControl_automated_qaTeam4@qwertysystem.net` (Pre-setup), `Spectra.env.GS_LIMIT_TC_PASSWORD`. Master Data Count Limit 1.000.
- Layar awal Global Settings > User > Custom Field (Client Limit) dibuka hook `beforeEach`; `## Test Steps` tidak mengulang langkah buka.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup Client Limit (fixture backend, dibaca saja): tepat 1.000 Custom Field dengan `Lim 500` berstatus Inactive sehingga field Active berjumlah 999. Volume dan status diatur backend sebelum spec ("disediakan tim BE"; TC menyatakan "volume dan status diatur backend sebelum TC"). Tidak ada data Dinamis milik spec.
- Cleanup (hook `after`): pulihkan status `Lim 500` dan volume ke nilai awal (disediakan tim BE); tutup dialog yang masih terbuka.
- Kemampuan teknis: pengaturan volume dan status Custom Field entitas Client Limit oleh backend (mekanisme tidak didefinisikan di TC, PRD, atau LLD).
- State global: Master Data Count Limit tidak diubah; volume dan status `Lim 500` dipulihkan seperti di atas.

## Test Steps

### TC-GS-UCF-454: Klik [+ Custom Field] saat 1.000 field memuat field Inactive tetap menampilkan dialog limit

1. Klik `[+ Custom Field]`
2. Verifikasi dialog `Limit Reached` (warning) dengan body `You've reached the platform limit of 1000 custom fields. Contact support if you need a higher limit.` dan tombol `[OK]` saja tanpa CTA upgrade
3. Verifikasi dialog tampil walau field Active hanya 999
4. Klik `[OK]`
5. Verifikasi dialog tertutup
6. Verifikasi form `New Custom Field` tidak terbuka

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Kelas harness: volume data (kelas e, bagian 3 prinsip 13e: 1.000 baris), terpisah dari spec 027 karena objek uji adalah komposisi volume yang memuat field Inactive, bukan perpindahan limit atau Create di batas.
- Dialog `Limit Reached` ditulis dengan `{limit}` tersubstitusi `1000` (angka polos tanpa pemisah ribuan) sesuai Expected TC.
- Pembagian TC lintas spec: TC-GS-UCF-87, 88, 90, 302, 364, 435, dan 453 (Master Data Count Limit Create lain) ada di spec 027.
- Temuan untuk QA:
  - TC-GS-UCF-454: volume 1.000 field dan status Inactive `Lim 500` diatur backend; mekanismenya tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis "disediakan tim BE" (S-13). TC tidak memiliki Post Condition.
  - Keputusan NC-20 (respons List membawa ceiling; dialog `Limit Reached` tampil saat klik `[+ Custom Field]`) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan. Hitungan limit memasukkan field Inactive sesuai TC dan PRD (§6 V-12).

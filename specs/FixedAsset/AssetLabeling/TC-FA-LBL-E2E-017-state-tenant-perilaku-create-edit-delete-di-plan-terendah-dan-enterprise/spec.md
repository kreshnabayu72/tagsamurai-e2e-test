---
id: TC-FA-LBL-E2E-017-state-tenant-perilaku-create-edit-delete-di-plan-terendah-dan-enterprise
title: "State Tenant: Perilaku Create/Edit/Delete di Plan Terendah dan Enterprise"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-106
  - TC-FA-LBL-476
coverage:
  web: automated
---

# State Tenant: Perilaku Create/Edit/Delete di Plan Terendah dan Enterprise

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor (login akun pertama di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; akun kedua lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Client | Pre-setup | Akun (Fixture) | Env | Langkah |
|---|---|---|---|---|
| Client plan terendah | #19 | `Fixture.assetLabeling.akun.totalControlPlanTerendah` | `Spectra.env.FA_TC_PLANTERENDAH_PASSWORD` | 1 sampai 19 |
| Client plan Enterprise | #20 | `Fixture.assetLabeling.akun.totalControlEnterprise` | `Spectra.env.FA_TC_ENTERPRISE_PASSWORD` | 20 sampai 40 |

- Environment variable: `FA_TC_PLANTERENDAH_PASSWORD`, `FA_TC_ENTERPRISE_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Dinamis (dibuat spec lewat UI, bersuffix `{runId}-017`; sisa dibersihkan di hook `after`): `Tier A 106 {runId}-017` (client plan terendah, TC-FA-LBL-106), `Tier B 106 {runId}-017` (client plan Enterprise, TC-FA-LBL-106), dan `Tier Flow 476 {runId}-017` (dibuat, diubah warnanya menjadi `#10B981`, lalu dihapus di tiap client, TC-FA-LBL-476).
- Kemampuan teknis: fixture BE untuk pembersihan label (lihat `suite.md`).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Client plan terendah: TC-FA-LBL-106 dan TC-FA-LBL-476

1. Klik `[+ Label]`
2. Isi Label Name dengan `Tier A 106 {runId}-017`
3. Klik `[Submit]`
4. Verifikasi toast `Success, label has been created.`
5. Verifikasi tidak ada dialog gating, tidak ada CTA upgrade, dan tidak ada kuota Label per paket
6. Tutup toast
7. Klik `[+ Label]`
8. Isi Label Name dengan `Tier Flow 476 {runId}-017`
9. Klik `[Submit]`
10. Verifikasi toast `Success, label has been created.`
11. Ketik Search `Tier Flow 476`, tekan Enter
12. Klik `⋯` pada baris `Tier Flow 476 {runId}-017` lalu `Edit`
13. Ubah warna menjadi `#10B981`
14. Klik `[Save]`
15. Verifikasi toast `Success, label has been updated.`
16. Klik `⋯` pada baris `Tier Flow 476 {runId}-017` lalu `Delete`
17. Klik `[Delete]` pada dialog
18. Verifikasi toast `Success, label has been deleted.`
19. Verifikasi tidak ada gating, upsell, atau batas berbeda pada ketiga aksi

### Client plan Enterprise: TC-FA-LBL-106 dan TC-FA-LBL-476

20. Ganti akun: Logout, login sebagai Total Control Client plan Enterprise `Fixture.assetLabeling.akun.totalControlEnterprise` (`Spectra.env.FA_TC_ENTERPRISE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
21. Klik `[+ Label]`
22. Isi Label Name dengan `Tier B 106 {runId}-017`
23. Klik `[Submit]`
24. Verifikasi toast `Success, label has been created.`
25. Verifikasi tidak ada dialog gating, tidak ada CTA upgrade, dan tidak ada kuota Label per paket
26. Tutup toast
27. Klik `[+ Label]`
28. Isi Label Name dengan `Tier Flow 476 {runId}-017`
29. Klik `[Submit]`
30. Verifikasi toast `Success, label has been created.`
31. Ketik Search `Tier Flow 476`, tekan Enter
32. Klik `⋯` pada baris `Tier Flow 476 {runId}-017` lalu `Edit`
33. Ubah warna menjadi `#10B981`
34. Klik `[Save]`
35. Verifikasi toast `Success, label has been updated.`
36. Klik `⋯` pada baris `Tier Flow 476 {runId}-017` lalu `Delete`
37. Klik `[Delete]` pada dialog
38. Verifikasi toast `Success, label has been deleted.`
39. Verifikasi tidak ada gating, upsell, atau batas berbeda pada ketiga aksi
40. Verifikasi UI dan hasil kedua client identik pada Create (langkah 4 sampai 5 dan langkah 24 sampai 25)

## Notes

- Spec ditulis per blok client dengan langkah Ganti akun eksplisit (langkah 20) karena akun pertama login di hook `before` (bagian 3a, 2026-10-30).
- Langkah penghubung (S-03): langkah 6 dan 26 (menutup toast sukses identik yang berulang sebelum asersi toast berikutnya, R-12), langkah 11 dan 31 (Search untuk menemukan baris target, R-16).
- Urutan TC: tiap client menjalankan TC-FA-LBL-106 (Create) lalu TC-FA-LBL-476 (Create, Edit, Delete) berurutan supaya tiap akun hanya login sekali; langkah tiap TC tetap mengikuti urutan TC (S-10).
- Absence (langkah 5, 19, 25, 39): toast sukses pada langkah sebelumnya menjadi anchor positif bahwa respons server selesai (bagian 8b butir 2).
- Alasan di atas sekitar 35 langkah (40 langkah): dua blok client berstruktur sama yang berdiri sendiri (kelas h, plan tier), tiap blok memakai data seed sendiri.
- Temuan untuk QA:
  - TC-FA-LBL-106 dan TC-FA-LBL-476 membandingkan "perilaku identik" tanpa menyebut elemen yang dibandingkan; spec membandingkan toast, dialog gating, CTA upgrade, dan kuota (langkah 5, 19, 25, 39, 40).
  - Nama plan terendah tidak disebut TC; akun disediakan tim FE (Pre-setup #19).
  - TC-FA-LBL-476 mengubah warna menjadi `#10B981` tanpa menyebut cara memilih warna; spec memakai kolom Hex pada Color Picker Overlay.

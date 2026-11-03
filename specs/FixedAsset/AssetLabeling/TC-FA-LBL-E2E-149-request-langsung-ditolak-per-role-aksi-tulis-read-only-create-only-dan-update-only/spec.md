---
id: TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only
title: "Request Langsung Ditolak per Role (Aksi Tulis): Read Only, Create-Only, dan Update-Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-441
  - TC-FA-LBL-442
  - TC-FA-LBL-443
  - TC-FA-LBL-444
  - TC-FA-LBL-445
  - TC-FA-LBL-446
  - TC-FA-LBL-447
coverage:
  web: automated
---

# Request Langsung Ditolak per Role (Aksi Tulis): Read Only, Create-Only, dan Update-Only

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Seluruh langkah berupa request langsung ke server lewat klien HTTP (bagian 8b butir 1): asersi hanya status respons dan state data yang dibaca lewat fixture BE; perilaku FE untuk respons yang sama diasersi di spec jalur form.
- Role yang diuji (sesi API; akun aktor hook `before` adalah Read Only, ganti sesi lewat langkah eksplisit; tidak ada login UI):

  | Role | Pre-setup | Akun | Env password |
  |---|---|---|---|
  | Read Only | #2 | `Fixture.assetLabeling.akun.readOnly` | `Spectra.env.FA_RO_PASSWORD` |
  | Create-Only | #3 | `Fixture.assetLabeling.akun.createOnly` | `Spectra.env.FA_CREATEONLY_PASSWORD` |
  | Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` |

- Seeding: label seed dibuat oleh Total Control (Pre-setup #1, `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`) lewat fixture BE di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Env var: `FA_RO_PASSWORD`, `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, dan `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak menulis ulang isinya.
- Data Dinamis (label seed milik spec, bersuffix `{runId}-149`, Color `Fixture.assetLabeling.warnaSeed`, Total Asset 0, bukan Default Label): `Direct Edit 442 {runId}-149`, `Direct Delete 443 {runId}-149`, `Direct Edit 444 {runId}-149`, `Direct Delete 445 {runId}-149`, `Direct Delete 447 {runId}-149`. Label `Direct Create 441`, `Direct Create 446` tidak di-seed (hasil request yang ditolak tidak boleh ada).
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data tanpa rahasia). Kunci yang dipakai spec ini:

  | Kunci | Nilai |
  |---|---|
  | `Fixture.assetLabeling.warnaSeed` | `#EF4444` (Color label seed) |
  | `Fixture.assetLabeling.akun.readOnly` | `readOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.createOnly` | `createOnly_automated_{namaCompany}@qwertysystem.net` |
  | `Fixture.assetLabeling.akun.updateOnly` | `updateOnly_automated_{namaCompany}@qwertysystem.net` |
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): klien HTTP untuk request langsung, sesi API (login API password) per role, fixture BE untuk seeding dan membaca state katalog serta jumlah entri Changelog Labels, System Log, dan Activity Log; endpoint tidak ditulis di TC (S-13).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Cleanup: hook `after` menghapus label seed milik spec lewat fixture BE berdasarkan ID, tanpa berasumsi seed berhasil penuh.

## Test Steps

### Persiapan baseline

1. Catat baseline jumlah entri Changelog Labels, System Log, dan Activity Log lewat fixture BE

### Read Only (TC-FA-LBL-441, TC-FA-LBL-442, TC-FA-LBL-443)

2. Gunakan sesi API Read Only (Pre-setup #2)
3. Kirim request langsung ke server sebagai Read Only: membuat label `Direct Create 441 {runId}-149`
4. Verifikasi server menolak dengan `403 Forbidden`
5. Verifikasi label `Direct Create 441 {runId}-149` tidak ada pada katalog
6. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline
7. Kirim request langsung ke server sebagai Read Only: mengubah nama `Direct Edit 442 {runId}-149` menjadi `Direct Edit 442 X {runId}-149`
8. Verifikasi server menolak dengan `403 Forbidden`
9. Verifikasi label tetap bernama `Direct Edit 442 {runId}-149`
10. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline
11. Kirim request langsung ke server sebagai Read Only: menghapus label bersih `Direct Delete 443 {runId}-149`
12. Verifikasi server menolak dengan `403 Forbidden`
13. Verifikasi label `Direct Delete 443 {runId}-149` masih ada pada katalog
14. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline

### Create-Only (TC-FA-LBL-444, TC-FA-LBL-445)

15. Ganti sesi API ke Create-Only (Pre-setup #3)
16. Kirim request langsung ke server sebagai Create-Only: mengubah nama `Direct Edit 444 {runId}-149` menjadi `Direct Edit 444 X {runId}-149`
17. Verifikasi server menolak dengan `403 Forbidden`
18. Verifikasi label tetap bernama `Direct Edit 444 {runId}-149`
19. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline
20. Kirim request langsung ke server sebagai Create-Only: menghapus label bersih `Direct Delete 445 {runId}-149`
21. Verifikasi server menolak dengan `403 Forbidden`
22. Verifikasi label `Direct Delete 445 {runId}-149` masih ada pada katalog
23. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline

### Update-Only (TC-FA-LBL-446, TC-FA-LBL-447)

24. Ganti sesi API ke Update-Only (Pre-setup #4)
25. Kirim request langsung ke server sebagai Update-Only: membuat label `Direct Create 446 {runId}-149`
26. Verifikasi server menolak dengan `403 Forbidden`
27. Verifikasi label `Direct Create 446 {runId}-149` tidak ada pada katalog
28. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline
29. Kirim request langsung ke server sebagai Update-Only: menghapus label bersih `Direct Delete 447 {runId}-149`
30. Verifikasi server menolak dengan `403 Forbidden`
31. Verifikasi label `Direct Delete 447 {runId}-149` masih ada pada katalog
32. Verifikasi jumlah entri Changelog Labels, System Log, dan Activity Log sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 8 (Security & Defense-in-Depth). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 1, 2, 15, 24 adalah navigasi, pembukaan atau penutupan modal, drawer, dialog, atau pengaturan state seeding tanpa `Verifikasi`; bukan bagian Expected TC.
- K-1: spec ini memuat TC kelas defense-in-depth (bagian 3 prinsip 13a) dengan Expected respons API; tumpang tindih dengan `tc-settings-asset-labeling-backend.md` dicatat BE pada tingkat endpoint.
- Asersi "tidak ada entri log baru" ditulis sebagai asersi jumlah entri Changelog Labels, System Log, dan Activity Log terhadap baseline (bagian 3 prinsip 13g: asersi jumlah bukan kelas g; S-12). Suite ini tidak memuat spec absence untuk TC ini, sehingga tidak ada rujukan ke spec lain (S-05).
- Penentuan akun dan sesi: seluruh langkah memakai sesi API, jadi ganti sesi antar-role (langkah penghubung) tidak memerlukan login UI (S-07).
- Temuan untuk QA:
  - Expected b TC-FA-LBL-441 sampai 447 "tidak ada entri log baru" tidak menyebut surface; spec memakai Changelog Labels, System Log, dan Activity Log (asersi jumlah dengan baseline).
  - Sesuai bagian 3 prinsip 13 (2026-10-30), asersi tidak-ada-entri atas request langsung yang ditolak lazimnya masuk spec absence; suite ini tidak memuat spec absence untuk TC-FA-LBL-441 sampai 450, 453, 455, 457, sehingga asersinya ditulis sebagai jumlah dengan baseline. Perlu keputusan pemilik proses bila ingin dipindah.
  - Nama baru pada TC-FA-LBL-442, 444, dan 449 ditulis `Direct Edit nnn X`; spec memakai nama bersuffix `{runId}` dan akhiran ` X` setelah suffix supaya unik per run.

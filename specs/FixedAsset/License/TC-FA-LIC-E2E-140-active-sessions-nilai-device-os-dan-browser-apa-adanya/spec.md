---
id: TC-FA-LIC-E2E-140-active-sessions-nilai-device-os-dan-browser-apa-adanya
title: "Active Sessions: Nilai Device / OS dan Browser Apa Adanya, Kosong Tampil ke `—`, dan Opsi Filter DISTINCT"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-599
coverage:
  web: automated
---

# Active Sessions: Nilai Device / OS dan Browser Apa Adanya, Kosong Tampil ke `—`, dan Opsi Filter DISTINCT

## Prerequisites

- Mode: FE+BE (backend nyata, tanpa mock).
- Akun: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #36 (fixture sesi Device / OS dan Browser, dipasang fixture BE di hook `before` dan dipulihkan ke Pre-setup #26 di hook `after`): tujuh sesi aktif pada client Paid Pre-setup #1, Online Users 7/25. Lima sesi cuplikan Pre-setup #26 (Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso) ditambah Maya Putri (Position Admin Aset, Division Divisi IT, IP Address `203.0.113.10`, Device / OS `Linux`, Browser `Opera`, Login Time 29/09/26 07:10, Last Activity 29/09/26 07:40) dan Joko Susilo (Position Staff Keuangan, Division Divisi Keuangan, IP Address `203.0.113.11`, Device / OS dan Browser kosong, Login Time 29/09/26 07:00, Last Activity 29/09/26 07:20). Identitas dan nilai data dirujuk lewat fixture `fixtures/fixed-asset-license.json` (belum ada, disiapkan tim FE).
- Data Dinamis: tidak ada. Spec ini hanya membaca tabel.
- Hook dan kemampuan suite (dinyatakan sekali di `suite.md`): fixture BE pemulih dan penukar Pre-setup #26 dan #36.

## Test Steps

### TC-FA-LIC-599: Device / OS dan Browser menampilkan nilai sesi apa adanya, `—` bila kosong, opsi Filter dari DISTINCT nilai

1. Klik tab Concurrent User
2. Verifikasi baris Maya Putri menampilkan Device / OS `Linux` dan Browser `Opera` sebagaimana diterima (di luar contoh nilai Windows, macOS, Android, iOS dan Chrome, Safari, Edge, Firefox, Mobile App)
3. Verifikasi baris Joko Susilo menampilkan Device / OS `—` dan Browser `—`
4. Klik ikon Filter pada toolbar, lalu buka dropdown `Device / OS`
5. Verifikasi opsi `Device / OS` dari DISTINCT nilai pada baris yang ada: Android, iOS, Linux, macOS, Windows
6. Buka dropdown `Browser`
7. Verifikasi opsi `Browser` dari DISTINCT nilai pada baris yang ada: Chrome, Edge, Mobile App, Opera, Safari
8. Pilih `Device / OS` = `Linux`, klik `[Apply]`
9. Verifikasi tabel menampilkan Maya Putri saja
10. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah penghubung tanpa `Verifikasi`: `[Clear Field]` lalu `[Apply]` di akhir (S-09).
- Spec ini memakai fixture sesi Pre-setup #36, berbeda dari fixture #26 spec Active Sessions lain.

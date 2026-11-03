---
id: TC-AC-ACTS-E2E-054-add-stock-rfid-reload-back-fisik-dan-pindah-tab-saat-sesi-aktif
title: "Add Stock RFID: Reload atau Tutup Tab, Back Fisik (Modal RFID Scan Stopped), dan Pindah Tab Browser saat List Berisi atau Sesi Aktif"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-159
  - TC-AC-ACTS-160
  - TC-AC-ACTS-161
  - TC-AC-ACTS-162
  - TC-AC-ACTS-796
coverage:
  web: automated
---

# Add Stock RFID: Reload atau Tutup Tab, Back Fisik (Modal RFID Scan Stopped), dan Pindah Tab Browser saat List Berisi atau Sesi Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #12 `RFID-ASSET-CORE-R5` (Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, TAG Type RFID).
- Kemampuan teknis: simulator pemindai RFID (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- Kemampuan teknis tambahan: penanganan dialog `beforeunload` browser (konfirmasi bawaan muncul, lalu dibatalkan) disediakan runner; tab browser kedua hanya dipakai untuk berpindah tab (S-08).
- TAG uji RFID (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | EPC | UID |
|---|---|---|
| TAG A | `Fixture.tagStock.rfidA.epc` (`E280116060000208A1B2C3`) | `Fixture.tagStock.rfidA.uid` (`A1B2C3D4E5F6`) |
| TAG B | `Fixture.tagStock.rfidB.epc` (`E280116060000208D4E5F6`) | `Fixture.tagStock.rfidB.uid` (`A1B2C3D4E5F7`) |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Ketik Search `RFID-ASSET-CORE-R5`, tekan Enter
2. Klik (⋯) baris SKU `RFID-ASSET-CORE-R5`, klik `Add Stock`

### TC-AC-ACTS-159: Reload dengan list kosong dan list berisi

3. Tekan F5
4. Verifikasi halaman Add Stock tampil
5. Verifikasi konfirmasi bawaan browser tidak muncul
6. Klik `[Add by Scan]`, scan TAG A, scan TAG B, lalu klik `[Stop]`
7. Tekan F5
8. Verifikasi konfirmasi bawaan browser muncul (teks ditentukan browser)
9. Batalkan konfirmasi browser agar tetap di halaman

### TC-AC-ACTS-796: Reload saat sesi scan aktif

10. Klik `[Add by Scan]`
11. Tekan F5
12. Verifikasi konfirmasi bawaan browser muncul (teks ditentukan browser)
13. Batalkan konfirmasi browser agar tetap di halaman

### TC-AC-ACTS-162: Berpindah tab browser saat sesi aktif

14. Pindah ke tab browser lain
15. Kembali ke tab ini
16. Verifikasi modal `RFID Scan Stopped` muncul saat tab kembali aktif
17. Klik `Continue Scan`

### TC-AC-ACTS-161: Back fisik, pilih Continue Scan

18. Tekan Back browser
19. Klik `Continue Scan`
20. Verifikasi modal tertutup
21. Verifikasi sesi scan berlanjut (widget scan masih tampil)

### TC-AC-ACTS-160: Back fisik, pilih Leave Page

22. Tekan Back browser
23. Verifikasi modal `RFID Scan Stopped` dengan body `The scan process was interrupted because you left this window.`, tombol `Leave Page` (kiri) dan `Continue Scan` (kanan)
24. Klik `Leave Page`
25. Verifikasi halaman Add Stock ditinggalkan
26. Verifikasi Total Registered SKU sama dengan baseline (hasil scan yang belum Submit hilang)

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 (membuka halaman Add Stock), pembentukan list precondition (scan lalu `[Stop]`), `[Add by Scan]` untuk membentuk sesi aktif, `Continue Scan` untuk melanjutkan sesi antar TC, dan pencatatan baseline Total Registered di hook `before`.
- Urutan TC dalam spec: 159, 796, 162, 161, 160 (kondisi sesi aktif dipertahankan sampai TC yang keluar halaman di akhir, S-10); sesi dari langkah 10 tetap aktif setelah `Continue Scan` (langkah 17), sehingga TC-AC-ACTS-161 dan TC-AC-ACTS-160 tidak memulai sesi baru.
- Absence konfirmasi bawaan browser (langkah 5) diletakkan sesudah anchor positif halaman Add Stock tampil (langkah 4), sesuai 8b butir 2.
- Tab browser kedua pada TC-AC-ACTS-162 hanya dipakai untuk berpindah tab; tidak ada asersi di tab itu.
- Temuan untuk QA:
  - TC-AC-ACTS-162 menyebut modal muncul "saat tab kembali aktif, bukan saat berpindah"; keadaan saat berpindah tidak dapat diamati dari tab yang tidak aktif sehingga hanya kemunculan saat kembali yang diasersi.
  - TC-AC-ACTS-160 Expected "hasil scan yang belum Submit hilang" tidak memberi langkah observasi; spec membandingkan Total Registered dengan baseline lewat kemampuan baca BE.
  - Teks konfirmasi browser ditentukan browser (TC-AC-ACTS-159 dan 796); hanya kemunculannya yang diasersi.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.

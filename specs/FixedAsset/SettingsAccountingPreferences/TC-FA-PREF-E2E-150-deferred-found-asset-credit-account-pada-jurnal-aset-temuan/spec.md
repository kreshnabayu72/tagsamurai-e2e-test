---
id: TC-FA-PREF-E2E-150-deferred-found-asset-credit-account-pada-jurnal-aset-temuan
title: "[DEFERRED] Found Asset Credit Account pada jurnal aset temuan"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-484
  - TC-FA-PREF-485
  - TC-FA-PREF-486
  - TC-FA-PREF-487
sourceRules: ["FAPREF-LOGIC-08f", "FAPREF-LOGIC-08g", "T-01", "FAPREF-LOGIC-10j", "FAPREF-LOGIC-08i"]
smoke: []
dependsOn: []
trace:
  "FAPREF-LOGIC-08f": 4
  "FAPREF-LOGIC-08g": [7, 8, 10]
  "T-01": [15, 24]
  "FAPREF-LOGIC-10j": [16, 25]
  "FAPREF-LOGIC-08i": [19, 28]
coverage:
  web: automated
---

# [DEFERRED] Found Asset Credit Account pada jurnal aset temuan

## Prerequisites

- Mode: FE+BE.
- Kelas harness: fungsional (alur lintas modul; TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun).
- Akun aktor: Total Control (PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env sama dengan spec lain di suite; perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup: Preferences nilai awal PC-1; Chart of Accounts PC-5 (`4-1500 – Pendapatan Lain-lain`, `1-2900 – Biaya Dikapitalisasi`); data PC-16 opname yang menemukan aset tidak tercatat (Physical Count & Reconciliation) dan jurnal aset temuan pada Export Journal. Data modul Physical Count & Reconciliation dan Export Journal disediakan tim FE setelah modul tersedia. Seed dan pemulihan lewat API sesuai `suite.md` (butir seed dan pemulihan).
- Nilai Found Asset Credit Account per TC (dibentuk lewat seed): `4-1500 – Pendapatan Lain-lain` untuk TC-FA-PREF-484 dan 487; kosong untuk TC-FA-PREF-485 dan 486.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences, opname dengan aset temuan, dan jurnal aset temuan berstatus ditahan atau sudah diekspor; pendaftaran aset temuan lewat UI Physical Count & Reconciliation; ekspor jurnal lewat UI Export Journal; pembacaan akun sisi kredit jurnal.
- State global yang diubah: Found Asset Credit Account company dan status jurnal aset temuan; dikembalikan ke nilai awal PC-1 oleh langkah pemulihan terakhir dan hook `after` (tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-484: Found Asset Credit Account dipakai sebagai akun sisi kredit aset temuan

1. Seed Found Asset Credit Account tersimpan "4-1500 – Pendapatan Lain-lain" dan opname yang menemukan aset tidak tercatat hingga tersimpan
2. Daftarkan aset temuan pada Physical Count & Reconciliation
3. Buka jurnal aset temuan pada Export Journal
4. Verifikasi jurnal aset temuan memakai akun "4-1500 – Pendapatan Lain-lain" pada sisi kredit

### TC-FA-PREF-485: Found Asset Credit Account kosong membuat aset temuan tetap teregister dan jurnalnya ditahan

5. Seed Found Asset Credit Account tersimpan kosong dan opname yang menemukan aset tidak tercatat hingga tersimpan
6. Daftarkan aset temuan pada Physical Count & Reconciliation
7. Verifikasi aset temuan tetap teregister
8. Verifikasi aset temuan disusutkan
9. Buka Export Journal
10. Verifikasi jurnal aset temuan ditahan saat Export Journal sampai akun diisi

### TC-FA-PREF-486: Perubahan Found Asset Credit Account dipakai jurnal aset temuan yang ditahan saat diekspor

11. Seed Found Asset Credit Account tersimpan kosong dan jurnal aset temuan ditahan hingga tersimpan
12. Buka Fixed Asset > Settings > Accounting > Preferences
13. Pilih "4-1500 – Pendapatan Lain-lain" pada Select Found Asset Credit Account
14. Klik [Save changes]
15. Verifikasi toast "Success, accounting preferences have been saved." tampil
16. Verifikasi tidak ada dialog Save Changes yang tampil
17. Buka Export Journal
18. Ekspor jurnal aset temuan yang ditahan
19. Verifikasi jurnal aset temuan diekspor dengan akun "4-1500 – Pendapatan Lain-lain" tanpa posting ulang

### TC-FA-PREF-487: Jurnal aset temuan yang sudah diekspor tidak berubah saat Found Asset Credit Account diganti

20. Seed Found Asset Credit Account tersimpan "4-1500 – Pendapatan Lain-lain" dan jurnal aset temuan sudah diekspor dengan akun "4-1500 – Pendapatan Lain-lain" hingga tersimpan
21. Buka Fixed Asset > Settings > Accounting > Preferences
22. Pilih "1-2900 – Biaya Dikapitalisasi" pada Select Found Asset Credit Account
23. Klik [Save changes]
24. Verifikasi toast "Success, accounting preferences have been saved." tampil
25. Verifikasi tidak ada dialog Save Changes yang tampil
26. Buka Export Journal
27. Buka jurnal aset temuan yang sudah diekspor
28. Verifikasi jurnal aset temuan yang sudah diekspor tetap memakai akun "4-1500 – Pendapatan Lain-lain"
29. Pulihkan Found Asset Credit Account ke kosong dan status jurnal aset temuan ke nilai awal lewat seed hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 12 dan 21 (membuka layar Preferences sesudah seed), langkah 9, 17, dan 26 (membuka Export Journal), langkah 29 (pemulihan state, S-09, R-08).
- Search tidak ditulis pada Export Journal karena TC tidak menyebut nama aset atau jurnal temuan; seed menyediakan satu jurnal aset temuan per TC sehingga baris target dikenali tim FE (lihat Temuan untuk QA).
- Seed per TC (langkah 1, 5, 11, 20) membentuk precondition tanpa bergantung hasil TC sebelumnya.
- Temuan untuk QA:
  - TC-FA-PREF-484 sampai 487 tidak menyebut nama aset temuan atau identitas jurnal aset temuan; spec tidak memakai Search dan bergantung pada seed yang disediakan tim FE (S-13).
  - TC-FA-PREF-485 Expected a memuat dua klausa ("teregister", "disusutkan") dan ditulis dua `Verifikasi` (langkah 7 dan 8, S-01).
  - TC-FA-PREF-486 dan 487 Expected a memuat dua klausa (toast, tanpa dialog) dan ditulis dua `Verifikasi` (S-01).
  - TC-FA-PREF-486 langkah TC "ekspor jurnal aset temuan yang ditahan" tidak menyebut label tombol ekspor; spec memakai teks TC.
  - Post Condition TC-FA-PREF-484 sampai 487 adalah kesimpulan dari Expected atau tanpa langkah observasi dan tidak diasersi terpisah (S-01).

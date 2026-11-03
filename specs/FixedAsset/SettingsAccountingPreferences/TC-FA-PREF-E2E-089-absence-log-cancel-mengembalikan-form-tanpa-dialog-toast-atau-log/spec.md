---
id: TC-FA-PREF-E2E-089-absence-log-cancel-mengembalikan-form-tanpa-dialog-toast-atau-log
title: "Absence Log: Klik [Cancel] Mengembalikan Form ke Nilai Tersimpan Tanpa Dialog, Toast, atau Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-274
  - TC-FA-PREF-577
coverage:
  web: automated
---

# Absence Log: Klik [Cancel] Mengembalikan Form ke Nilai Tersimpan Tanpa Dialog, Toast, atau Log

## Prerequisites

- Mode: FE+BE.
- Kelas harness: g (asersi absence dialog, toast, request, dan log).
- Akun aktor: Total Control (Pre-setup PC-8: Rina Anggraini, tampil "Rina A") `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD` (nama env perlu dikonfirmasi tim FE sebelum didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences).
- Data Pre-setup (hanya dibaca, tidak diubah): Preferences nilai awal PB-1 untuk TC-FA-PREF-274 dan PC-1 untuk TC-FA-PREF-577 (setara: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date); akun Chart of Accounts PB-2; Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6); Changelog Preferences berisi 1 entri Create (PB-1). Seed disediakan tim FE/BE (lihat `suite.md`, butir seed dan pemulihan lewat API); seed ulang ke nilai awal PC-1 dilakukan lewat langkah penghubung (langkah 16).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): pengamatan request jaringan dari browser (hanya mengamati, tanpa mengubah respons) untuk klausa "tidak ada permintaan ke server" pada langkah 11; kemampuan baca BE jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline sebelum aksi, bagian 8b butir 10 dan S-12).
- Flag Guided Tooltip halaman Preferences disetel true oleh hook suite `before` (lihat `suite.md`) sehingga walkthrough tidak menutupi layar.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-274: Klik [Cancel] mengembalikan form ke nilai tersimpan tanpa dialog, toast, atau log

1. Klik ikon View history
2. Catat jumlah baris pada modal Changelog (baseline)
3. Klik ikon [✕] di header modal Changelog
4. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
5. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
6. Klik [Cancel]
7. Verifikasi Select In-service Date Source kembali menampilkan "Activation date"
8. Verifikasi CurrencyInput Default Capitalization Threshold kembali menampilkan "Rp 5.000.000,00"
9. Verifikasi tidak ada dialog yang tampil
10. Verifikasi tidak ada toast yang tampil
11. Verifikasi tidak ada permintaan ke server yang terkirim akibat klik [Cancel]
12. Verifikasi [Save changes] dan [Cancel] berstatus Disabled karena form pristine
13. Klik ikon View history
14. Verifikasi jumlah baris pada modal Changelog sama dengan baseline langkah 2 (1 baris)
15. Klik ikon [✕] di header modal Changelog

### TC-FA-PREF-577: Cancel pada form dirty mengembalikan nilai tersimpan tanpa dialog, toast, dan log

16. Seed ulang Preferences ke nilai awal PC-1 hingga tersimpan
17. Muat ulang halaman dengan F5
18. Catat jumlah baris Changelog Preferences, jumlah entri System Log Rina Anggraini, dan jumlah entri Activity Log FAMS (baseline)
19. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
20. Klik [Cancel]
21. Verifikasi CurrencyInput Default Capitalization Threshold kembali "Rp 5.000.000,00"
22. Verifikasi tidak ada dialog
23. Verifikasi tidak ada toast
24. Verifikasi jumlah baris Changelog sama dengan baseline langkah 18
25. Verifikasi jumlah entri System Log Rina Anggraini sama dengan baseline langkah 18
26. Verifikasi jumlah entri Activity Log FAMS sama dengan baseline langkah 18

## Notes

- P-5: spec ini adalah spec absence (kelas g); aksi [Cancel] pada form dirty adalah pemicu kondisi yang diasersi tidak menghasilkan dialog, toast, request, atau log. Tiap TC punya baseline sendiri (S-12, S-05).
- Langkah penghubung (S-03): langkah 3 dan 15 (menutup modal), langkah 16 dan 17 (seed ulang seri PC-1 dan muat ulang agar form memuat nilai seed). Layar Preferences dibuka hook `beforeEach` suite.
- Anchor absence (bagian 8b butir 2 dan 11): asersi tidak ada dialog dan toast (langkah 9, 10, 22, 23) diletakkan segera setelah [Cancel] (langkah 6 dan 20), dan nilai form yang kembali (langkah 7, 8, 21) membuktikan [Cancel] sudah diproses; absence log memakai baseline (langkah 2 dan 18).
- Form pristine di akhir tiap TC karena [Cancel] mengembalikan nilai tersimpan; spec tidak berakhir dengan form dirty.
- Temuan untuk QA:
  - TC-FA-PREF-274 Post Condition butir b ("Tidak ada entri log baru pada Changelog, System Log, maupun Activity Log") tidak punya langkah observasi untuk System Log dan Activity Log (langkah TC hanya menghitung baris modal Changelog); hanya Changelog diasersi dan Post Condition tidak diklaim teruji untuk dua surface lain (S-05).
  - TC-FA-PREF-274 Expected d ("Tidak ada permintaan ke server yang terkirim akibat klik [Cancel]") tidak punya cara cek di TC; spec memakai pengamatan request jaringan sebagai kemampuan tim FE.
  - TC-FA-PREF-577 langkah 4 menghitung baris log tiga surface sedangkan precondition d hanya menyebut pencatatan jumlah awal; spec menambahkan langkah Catat baseline (langkah 18).
  - TC-FA-PREF-274 memakai seri fixture PB dan TC-FA-PREF-577 memakai seri PC; spec mengasumsikan nilai awal keduanya setara (Catatan TC: seri fixture seed terisolasi).

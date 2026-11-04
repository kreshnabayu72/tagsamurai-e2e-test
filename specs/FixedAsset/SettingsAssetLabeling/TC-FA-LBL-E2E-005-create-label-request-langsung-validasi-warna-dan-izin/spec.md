---
id: TC-FA-LBL-E2E-005-create-label-request-langsung-validasi-warna-dan-izin
title: "Create Label lewat request langsung: validasi warna dan penolakan Read Only"
priority: Critical
caseType: Negative
status: draft
sourceRules:
  - E-FALB-08
  - F-FALB-02.k2
  - E-FALB-09
  - FALB-LOGIC-03c
  - FALB:must-not/menyimpan-kode-warna-yang-bukan-6-digit-heksadesimal-ber
  - FALB-LOGIC-05a
coverage:
  web: automated
---

# Create Label lewat request langsung: validasi warna dan penolakan Read Only

## Prerequisites

- Mode: FE+BE
- Akun: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`) dan Read Only `DU-02` (env `FA_RO_EMAIL`, `FA_RO_PASSWORD`). Seluruh langkah memakai sesi API `DU-01` dan `DU-02`; halaman tidak dibuka.
- Data uji: `DU-10` (kode hex valid), `DU-12` (kode hex tidak valid, satu nilai per kategori), `DU-51` (nama label untuk semua request Create; label belum ada saat run dan baru tersimpan di langkah 14).
- Kemampuan teknis: klien HTTP untuk request langsung ke server, sesi API aktor `DU-01` dan `DU-02` (login API password, token tidak dihitung sebagai sesi web), dan fixture BE untuk membaca katalog Label; semuanya disediakan tim FE/BE (dinyatakan di `suite.md`).
- Cleanup: hook `after` menghapus label `DU-51` lewat sesi API `DU-01` bila ada; cleanup tidak berasumsi request di langkah 14 berhasil.
- Spec ini membuat data (label `DU-51`) sehingga dipisah dari spec yang tidak membuat data.

## Test Steps

1. Baca jumlah label katalog lewat fixture BE, catat sebagai baseline

### E-FALB-09: Read Only membuat Label lewat request langsung

2. Kirim request langsung Create Label dengan sesi API `DU-02`: nama `DU-51`, warna `DU-10`
3. Verifikasi respons server menolak request

### FALB-LOGIC-05a: Pengelolaan katalog dinaungi role Manage Asset Master Data

4. Verifikasi jumlah label katalog (fixture BE) sama dengan baseline langkah 1

### F-FALB-02.k2: Format warna tidak valid ditolak server

5. Kirim request langsung Create Label dengan sesi API `DU-01`: nama `DU-51`, warna kode lebih dari 6 digit (`DU-12`)
6. Verifikasi respons server menolak request
7. Kirim request langsung Create Label dengan sesi API `DU-01`: nama `DU-51`, warna kode 6 digit tanpa awalan `#` (`DU-12`)
8. Verifikasi respons server menolak request

### FALB-LOGIC-03c: Server memvalidasi format warna pada permintaan langsung

9. Kirim request langsung Create Label dengan sesi API `DU-01`: nama `DU-51`, warna kode berisi karakter non-heksadesimal (`DU-12`)
10. Verifikasi respons server menolak request

### FALB:must-not/menyimpan-kode-warna-yang-bukan-6-digit-heksadesimal-ber: Kode warna bukan #RRGGBB tidak disimpan dari request langsung

11. Verifikasi jumlah label katalog (fixture BE) sama dengan baseline langkah 1, sehingga tidak ada label berkode warna tidak valid yang tersimpan

### E-FALB-08: Server memvalidasi format warna pada request langsung

12. Kirim request langsung Create Label dengan sesi API `DU-01`: nama `DU-51`, warna kode kurang dari 6 digit (`DU-12`)
13. Verifikasi respons server menolak request dengan pesan `Invalid color format`
14. Kirim request langsung Create Label dengan sesi API `DU-01`: nama `DU-51`, warna `DU-10`
15. Verifikasi respons server menerima request
16. Verifikasi label `DU-51` tersimpan di katalog (fixture BE) dengan warna `DU-10`, huruf besar dan kecil tidak dibedakan

## Notes

- Langkah penghubung (S-03): langkah 1 mencatat baseline jumlah label sebelum request pertama; langkah 4 dan 11 membandingkan jumlah label terhadap baseline itu (bagian 8b butir 2).
- Asersi request langsung hanya status respons, pesan penolakan, dan state data lewat fixture BE; pengalihan halaman, toast, atau tampilan tidak diasersi (bagian 8b butir 1). Perilaku FE untuk kode warna tidak valid ada di spec 003.
- Pembagian klausa lintas spec: `FALB-LOGIC-03c` diasersi di sini untuk validasi server atas request langsung; validasi real-time di UI ada di spec 003. `FALB:must-not/menyimpan-kode-warna-yang-bukan-6-digit-heksadesimal-ber` diasersi di sini untuk jalur request langsung; jalur form ada di spec 003. `FALB-LOGIC-05a` diasersi di sini untuk penolakan server atas akun tanpa role "Manage Asset Master Data"; tampilan per role ada di spec 006. `FALB-LOGIC-05a` juga dikutip spec 007.
- Langkah 4 di bawah `FALB-LOGIC-05a` sekaligus bukti penolakan `E-FALB-09` (langkah 2 dan 3): jumlah label tidak berubah sesudah request Read Only ditolak.
- Temuan PRD / aturan ditahan: klausa `E-FALB-08` bahwa hex huruf kecil dinormalisasi ke huruf kapital adalah klausa aturan `FALB-LOGIC-03d` yang ditahan, sehingga langkah 16 tidak membandingkan huruf besar dan kecil.
- Kategori kode tidak valid dibagi ke empat blok: lebih dari 6 digit dan 6 digit tanpa awalan `#` di `F-FALB-02.k2` (langkah 5 sampai 8), karakter non-heksadesimal di `FALB-LOGIC-03c` (langkah 9), kurang dari 6 digit di `E-FALB-08` (langkah 12); semuanya nilai `DU-12`.

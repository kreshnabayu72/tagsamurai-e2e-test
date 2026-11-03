---
id: TC-FA-TAG-E2E-121-print-qr-validasi-quantity-v-39-dan-batas-bagian-2
title: "Print QR: Quantity tidak menerima huruf, pulih setelah invalid, dan batas bawah 1"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-487
  - TC-FA-TAG-488
  - TC-FA-TAG-489
coverage:
  web: automated
---

# Print QR: Quantity tidak menerima huruf, pulih setelah invalid, dan batas bawah 1

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun ini (lihat `suite.md`).
- Data: tanpa data khusus. TC-489 menekan [Start Print] dengan `Quantity` 1 sehingga satu kode QR dibuat backend.
- Kemampuan teknis (disediakan tim FE/BE): pengamat jaringan atas permintaan cetak Start Print (`Spectra.intercept` mode amati saja); dialog cetak browser (tingkat OS) yang teramati dan ditutup oleh harness; pembersihan kode QR hasil cetak dari registri Global lewat fixture backend.
- State global yang dipulihkan: kode QR yang dibuat TC-489 dihapus dari registri Global di hook `after`.

## Test Steps

1. Klik tombol `Print QR` di toolbar tab Paired.
2. Verifikasi Dialog Print QR terbuka.

### TC-487: Quantity tidak menerima karakter huruf

3. Ketik `abc` pada `Quantity`.
4. Verifikasi field `Quantity` tidak menampilkan karakter huruf `abc` yang diketik (hanya angka yang diterima).

### TC-488: Quantity valid kembali setelah invalid

5. Isi `Quantity` dengan 0.
6. Verifikasi Preview menampilkan "Enter a quantity to see the preview."
7. Isi `Quantity` dengan 3.
8. Verifikasi Preview memuat sel `1` sampai `3`.
9. Verifikasi pesan "Quantity must be a whole number from 1 to 100" hilang.

### TC-489: Quantity 1 (batas bawah) valid

10. Isi `Quantity` dengan 1.
11. Verifikasi Preview memuat sel `1`.
12. Verifikasi tidak ada pesan "Quantity must be a whole number from 1 to 100".
13. Klik [Start Print].
14. Verifikasi request cetak diproses.
15. Verifikasi Toast "Success, QR labels have been sent to print."
16. Tutup dialog cetak browser.

## Notes

- Langkah penghubung: dialog dibuka sekali di langkah 1 dan dipakai ketiga TC; langkah 16 menutup dialog cetak browser yang terbuka setelah Start Print.
- Anchor positif (S-03): langkah 2 (Dialog Print QR terbuka) menjadi anchor absence TC-487; langkah 11 (Preview sel `1`) menjadi anchor absence pesan di langkah 12 TC-489; langkah 8 menjadi anchor langkah 9 TC-488. Ketiganya tidak ada di Expected TC.
- Pembagian TC lintas spec: TC-482 sampai TC-486 ada di spec 120.
- Temuan untuk QA:
  - TC-489 diberi label Manual Only karena dialog cetak browser tingkat OS; spec tetap memuatnya dan kemampuan menutup dialog cetak browser dicatat di Prerequisites. TC tidak menyebut cara mengamati "request cetak diproses"; spec memakai pengamat jaringan.
  - TC-489 tidak punya Expected untuk pembuatan satu kode QR (Post Condition "Satu kode QR dibuat backend" tanpa langkah observasi), jadi tidak diasersi.
  - TC-488 hanya mengasersi hilangnya pesan setelah nilai valid; kemunculan pesan untuk nilai 0 tidak ada di Expected, sehingga tidak diasersi di spec ini.

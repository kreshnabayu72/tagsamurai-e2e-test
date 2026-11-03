---
id: TC-FA-FAAM-E2E-245-tag-type-tanpa-objek-tugas-dan-pending-changes
title: "TAG Type Ber-Aset: Edit Tidak Membuat Objek Tugas atau Dokumen dan Menu TAG Tanpa Pending Changes"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-829
coverage:
  web: automated
---

# TAG Type Ber-Aset: Edit Tidak Membuat Objek Tugas atau Dokumen dan Menu TAG Tanpa Pending Changes

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`) dengan akses menu Approvals, dokumen transaksi (Change Document), dan Fixed Asset > TAG. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup: No. 10 dan No. 29 (`Dell Latitude`, Total Asset 42, TAG Type `RFID`+`QR`). `Dell Latitude` tidak dapat digandakan dan menjadi target Edit TAG Type; hook `before` dan hook `after` menyediakannya ulang ke keadaan Pre-setup No. 10 dan No. 29 lewat seed API (kemampuan disediakan tim BE/FE; Post Condition TC: "Perubahan TAG Type tersimpan; `Dell Latitude` disediakan ulang"). Efek: Last Updated `Dell Latitude` berubah; suite berjalan serial. Pernyataan ini belum ada di `suite.md` (lihat Temuan untuk QA).
- Kemampuan teknis: membaca jumlah entri menu Approvals dan menu dokumen transaksi (Change Document); membuka Fixed Asset > TAG.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan `Dell Latitude` ke Pre-setup No. 10 dan No. 29.
- State global yang diubah: TAG Type `Dell Latitude` (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-829: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

1. Buka menu Approvals
2. Catat jumlah entri Approvals sebagai nilai A
3. Buka menu dokumen transaksi (Change Document)
4. Catat jumlah entri dokumen transaksi sebagai nilai D
5. Buka Fixed Asset > Settings > Asset Master > Asset Name
6. Ketik Search `Dell Latitude`, tekan Enter
7. Klik `⋯` baris `Dell Latitude` lalu `Edit`
8. Lepas `RFID` dan pilih `NFC` pada TAG Type
9. Klik `[Save]`
10. Klik `[Save]` pada dialog Change TAG Type
11. Tunggu aksi selesai
12. Buka menu Approvals
13. Verifikasi jumlah entri Approvals sama dengan nilai A pada langkah 2
14. Buka menu dokumen transaksi (Change Document)
15. Verifikasi jumlah entri dokumen transaksi sama dengan nilai D pada langkah 4
16. Buka Fixed Asset > TAG
17. Verifikasi menu TAG memuat tab `Paired` dan `To Be Returned`
18. Verifikasi tidak ada tab, tabel, atau record Pending Changes (tanpa `Start Date` dan tanpa status `In Progress`)
19. Sediakan ulang `Dell Latitude` ke keadaan Pre-setup No. 10 dan No. 29 lewat seed API

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 3, 5, 12, 14, 16 (navigasi), langkah 2 dan 4 (mencatat baseline), langkah 6 (Search untuk menemukan baris target), langkah 11 (menunggu `[Save]` selesai sebelum pindah surface), dan langkah 19 (pemulihan fixture; S-09).
- Langkah 18 adalah asersi absence dengan anchor positif langkah 17 (tab `Paired` dan `To Be Returned` tampil pada surface yang sama; bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-FAAM-665 dan 828 ada di spec 228.
- Temuan untuk QA:
  - TC-FA-FAAM-829 butir a ("tidak ada tugas, dokumen, atau approval baru yang merujuk `Dell Latitude`") diasersi sebagai kesamaan jumlah entri terhadap baseline pada dua menu karena TC tidak memberi cara memfilter entri menurut Asset Name.
  - `Dell Latitude` (Pre-setup No. 10) dimutasi; S-06 mensyaratkan fixture pemulihan dinyatakan di `suite.md` (belum ada).

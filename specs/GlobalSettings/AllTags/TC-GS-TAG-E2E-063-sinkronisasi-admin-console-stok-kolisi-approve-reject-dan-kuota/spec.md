---
id: TC-GS-TAG-E2E-063-sinkronisasi-admin-console-stok-kolisi-approve-reject-dan-kuota
title: "Sinkronisasi Admin Console: Pemakaian Stok, Kolisi sebagai Activation Collision, Approve, Reject, dan Perubahan Alokasi Kuota"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-304
  - TC-GS-TAG-305
  - TC-GS-TAG-306
  - TC-GS-TAG-307
  - TC-GS-TAG-308
coverage:
  web: automated
---

# Sinkronisasi Admin Console: Pemakaian Stok, Kolisi sebagai Activation Collision, Approve, Reject, dan Perubahan Alokasi Kuota

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini mengubah data registri dan stok lewat aktivasi, Approve, dan Reject; perubahan alokasi kuota (state global) dijalankan terakhir.
- Akun aktor (ganti akun eksplisit; hasil di Admin Console dan Approvals diasersi di sesi modul itu):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun ini sebagai default suite.
  - Principal approver (Mira Anggraini) `principalApprover_automated@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`, untuk Admin Console > Approvals > TAG Stock (TC-GS-TAG-305 dan 307, sesi UI) dan untuk Approve TC-GS-TAG-306 lewat sesi API aktor. Kesamaan akun ini dengan env var terdaftar perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
  - Akun Admin Console Client A untuk Admin Console > TAG Stock (TC-GS-TAG-304): tidak ada di Pre-setup TC; akun dan kredensial disediakan tim FE (S-13).
  - Akun Admin Console Device Allocation (TC-GS-TAG-308): tidak ada di Pre-setup TC; disediakan tim FE (S-13). Sesi API aktor, hanya pemicu.
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu GPS `1 of 30`) dan stok resmi Client A: GPS `356938035643001` dan `356938035643003` Available, `356938035643002` Damaged/Missing (Device Name `Teltonika FMB920`, SKU `SKU-GPS-01`, Brand `Teltonika`, Model/Type `FMB920`). Opsi mandiri aktif; katalog memuat Device Name `Queclink GV300` (Brand `Queclink`) untuk Template Self-Purchased. IMEI `356938035643101` (belum ada di stok maupun registri) untuk Self-Purchased baru; IMEI `356938035643201` In Use di Client B (kolisi). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec, sebelum TC-GS-TAG-307 (subject kolisi pending), dan sebelum TC-GS-TAG-308.
- Data Dinamis: Approval Note `Catatan approval {runId}-063` pada TC-GS-TAG-306.
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Principal approver (Approve, langkah 25) dan akun Device Allocation (langkah 56).
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A, stok resmi, kepemilikan In Use di Client B, dan subject Activation Collision pending; sesi API Principal untuk Approve subject Activation Collision (hingga tersimpan); sesi API Admin Console Device Allocation untuk mengubah alokasi GPS Client A (30 menjadi 40); penanda event selesai diproses (Eventual); baca jumlah entri Activity Log dan jumlah baris Event Log Tab Activate TAG sebelum aksi (N; asersi memakai selisih terhadap N). Langkah dan selektor Admin Console TAG Stock, Approvals, dan Device Allocation tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan alokasi GPS Client A ke 30, kembalikan Seed Registri A, stok resmi, dan subject Approvals lewat fixture BE; sesi ke Total Control Client A.
- Suite serial (`parallel: false`). State global yang diubah: alokasi GPS Client A (Admin Console), dipulihkan hook `after`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-304: Aktivasi Official dan Self-Purchased, pemakaian stok

1. Klik `+ Activate TAG`
2. Pilih `GPS` pada overlay `Select TAG Type`
3. Klik `Continue` pada popup `Ready to Activate a TAG`
4. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
5. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643001`
6. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643101`
7. Klik `Submit` lalu konfirmasi
8. Tunggu aksi selesai (dialog tertutup, tombol aktif kembali)
9. Ganti akun ke akun Admin Console Client A, buka Admin Console > TAG Stock
10. Ketik Search `356938035643001`, tekan Enter
11. Verifikasi unit stok resmi `356938035643001` berstatus `In Use`
12. Ganti isi kotak search dengan `356938035643101`, tekan Enter
13. Verifikasi unit baru `356938035643101` tercatat di TAG Stock (Jalur B)

### TC-GS-TAG-305: Kolisi masuk Approvals sebagai Activation Collision

14. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All
15. Klik `+ Activate TAG`
16. Pilih `GPS` pada overlay `Select TAG Type`
17. Klik `Continue` pada popup `Ready to Activate a TAG`
18. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
19. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643201`
20. Klik `Submit` lalu konfirmasi, hingga baris `356938035643201` berstatus Waiting for Approval
21. Catat nilai kartu GPS (terpakai)
22. Ganti akun ke Principal approver, buka Admin Console > Approvals > TAG Stock Tab Active
23. Verifikasi subject `Activation Collision` untuk `356938035643201` tampil di Tab Active untuk approver Principal

### TC-GS-TAG-306: Approve kolisi

24. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All
25. Setujui subject `356938035643201` lewat sesi API Principal dengan Approval Note `Catatan approval {runId}-063` hingga tersimpan
26. Verifikasi status tag `356938035643201` `Available` tanpa muat ulang halaman
27. Verifikasi kartu GPS terpakai tidak berubah dari nilai yang dicatat
28. Buka menu baris tag `356938035643201`, lalu klik `TAG Log`
29. Verifikasi entri `TAG Approved by [pelaku approver]` dengan Approval Note `Catatan approval {runId}-063`
30. Tutup popup TAG Log

### TC-GS-TAG-307: Reject kolisi

31. Pulihkan subject kolisi `356938035643201` pending dan tag Waiting for Approval lewat fixture BE, muat ulang halaman, lalu klik Tab All
32. Catat nilai kartu GPS (terpakai N)
33. Buka Global Settings > Activity Log dan catat jumlah entri, lalu buka Event Log di Tab All dan catat jumlah baris Tab Activate TAG
34. Ganti akun ke Principal approver, buka Admin Console > Approvals > TAG Stock Tab Active
35. Tolak subject `356938035643201`, lalu Submit
36. Tunggu aksi selesai (dialog tertutup, tombol aktif kembali)
37. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All
38. Verifikasi kartu GPS terpakai berkurang 1 dari N
39. Verifikasi baris `356938035643201` hilang dari registri
40. Buka Global Settings > Activity Log
41. Verifikasi Activity Log tidak memuat entri Reject baru (jumlah entri sama dengan yang dicatat)
42. Buka Global Settings > TAG Tab All, lalu buka Event Log > Tab Activate TAG
43. Verifikasi Event Log tidak memuat entri Reject baru (jumlah baris sama dengan yang dicatat)
44. Tutup modal Event Log
45. Klik `+ Activate TAG`
46. Pilih `GPS` pada overlay `Select TAG Type`
47. Klik `Continue` pada popup `Ready to Activate a TAG`
48. Isi Template Device Name `Queclink GV300`, Brand `Queclink`
49. Tambahkan lewat entri manual (ketik di input lalu klik `Add`) `356938035643201`
50. Klik `Submit` lalu konfirmasi, hingga sukses
51. Buka menu baris tag `356938035643201`, lalu klik `TAG Log`
52. Verifikasi TAG Log memuat entri aktivasi baru
53. Verifikasi TAG Log tag baru tidak memuat entri lama
54. Tutup popup TAG Log

### TC-GS-TAG-308: Kartu counter mengikuti perubahan alokasi kuota

55. Pulihkan Seed Registri A dan alokasi GPS Client A 30 lewat fixture BE, muat ulang halaman, lalu klik Tab All
56. Ubah alokasi GPS Client A dari 30 menjadi 40 di Admin Console > Device Allocation lewat sesi API akun Admin Console Device Allocation hingga tersimpan
57. Verifikasi kartu GPS menampilkan `1 of 40` tanpa muat ulang halaman registri
58. Verifikasi kartu GPS menampilkan `39 remaining`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (58 langkah nominal). Alasan: lima TC satu topik (efek aktivasi, kolisi, dan alokasi pada Admin Console/Approvals terhadap registri) dengan satu dataset (Seed Registri A dan stok GPS Client A); tiap blok berdiri sendiri karena data dipulihkan lewat fixture BE di langkah 31 dan 55, dan bagian sesudah tiap ganti akun tetap bermakna. Langkah aktivasi (langkah 1 sampai 7, 15 sampai 20, 45 sampai 50) disalin utuh dari alur Activate sebagai pembuka tiap TC (S-04).
- Langkah ganti akun eksplisit: 9, 14, 22, 24, 34, 37.
- Reject pada Approvals (langkah 35) dijalankan Principal lewat ganti akun eksplisit; hasil diasersi di sesi Client A setelah ganti akun lagi. Approve (langkah 25) dijalankan lewat sesi API Principal sementara sesi Total Control Client A tetap di Tab All, sehingga status diamati tanpa muat ulang halaman (langkah 26).
- Perubahan urutan (S-05 butir terakhir): TC-GS-TAG-306 mengikuti TC-GS-TAG-305 karena memakai subject pending yang sama (precondition TC-GS-TAG-306 identik dengan hasil TC-GS-TAG-305); TC-GS-TAG-308 (mengubah alokasi kuota, state global) di akhir dan didahului pemulihan Seed Registri A karena `1 of 40` mensyaratkan keadaan awal.
- Pengecualian P-1: asersi bahwa tidak ada entri Reject baru di Activity Log dan Event Log (langkah 41 dan 43; D-1) memakai baseline jumlah entri yang dicatat sebelum aksi Reject (langkah 33) dan didahului penurunan kartu GPS (langkah 38) sebagai anchor pemicu.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 9, 14, 22, 24, 34, 37 (ganti akun dan navigasi), 21, 32, dan 33 (baseline), 30, 44, dan 54 (menutup popup atau modal), 31 dan 55 (memulihkan data lewat fixture BE), 40 dan 42 (navigasi ke log), 8 dan 36 (menunggu aksi konfirmasi selesai sebelum ganti akun), 10 dan 12 (Search untuk menemukan baris target), 25 (Approve lewat sesi API sebagai pemicu).
- Asersi tambahan di luar Expected TC (S-03): langkah 38 dan 52 sebagai anchor positif sebelum absence (bagian 8b butir 2).
- Temuan untuk QA:
  - Q-9: langkah dan selektor Admin Console TAG Stock, Approvals, dan Device Allocation tidak didefinisikan; verifikasi hanya sejauh Expected TC.
  - Q-2: Pre-setup TC memakai `principalApprover_automated`, sedangkan `.env.example` mendaftarkan `totalControlPrincipal_automated_qaTeam1` (GS_PRINCIPAL_TC); kesamaan perlu dikonfirmasi tim FE saat tahap script (Q-2, kategori B).
  - TC-GS-TAG-306 Expected a "Status `Available` (SSE tanpa refresh)": Approve dijalankan lewat sesi API Principal sementara sesi Total Control Client A tetap di Tab All, sehingga status diamati tanpa muat ulang (langkah 26); langkah dan endpoint sesi API tidak didefinisikan di TC, PRD, atau LLD (Q-9).
  - TC-GS-TAG-307 Expected b "Tidak ada entri log Reject di modul ini" tidak menyebut surface log; spec memakai Activity Log dan Event Log Tab Activate TAG (baseline jumlah entri).
  - TC-GS-TAG-307 langkah 3 "Aktivasi ulang kode yang sama ... hingga sukses": `356938035643201` masih In Use di Client B sehingga aktivasi ulang berpotensi kembali Waiting for Approval; Expected b "TAG Log tag baru tidak memuat entri lama" tidak menyebut entri lama mana; spec mengasersi tidak adanya entri lama setelah anchor entri aktivasi baru.
  - TC-GS-TAG-304 Expected hanya menyebut `In Use` dan unit baru di TAG Stock; kolom TAG Stock tidak dinamai TC.
  - Post Condition TC-GS-TAG-306 butir a dan b identik dengan Expected a dan c; Post Condition TC-GS-TAG-307 identik dengan Expected a dan b.
  - Q-4: identifier tetap; kartu GPS `1 of 30` dan `1 of 40` valid hanya bila Seed Registri A dipulihkan (langkah 55).

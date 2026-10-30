---
id: TC-GS-TAG-E2E-089-logging-delete-single-dan-bulk-event-log-activity-log
title: "Pencatatan Delete Single dan Bulk: Event Log, Activity Log, dan TAG Type Mixed"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-267
  - TC-GS-TAG-268
coverage:
  web: automated
---

# Pencatatan Delete Single dan Bulk: Event Log, Activity Log, dan TAG Type Mixed

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A Sari Dewi (`Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` tidak mengganti sesi.
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Hook `after` suite memulihkan Seed Registri A secara idempotent (pernyataan hook di `suite.md`).
- Data Pre-setup: Seed Registri A (dipulihkan ke kondisi awal oleh hook `before` lewat fixture BE; mekanisme disediakan tim FE/BE, lihat Temuan untuk QA). Target hapus milik dataset ini: DD-12 `E2801160600002054D8A0012` (RFID Object, Self-Purchased, Available; Tab All), DD-15 `E28011606000020F00000001` (RFID Object, Official, Available; Tab Not Paired), dan DD-04 `AABBCCDDEE80` (BLE, Damaged/Missing; Tab Not Paired). Sesuai aturan data destruktif (bagian 2 konvensi), aksi Delete dikonfirmasi sungguhan di environment automation.
- Baseline log: Event Log dan Activity Log menumpuk antar spec (tidak dibersihkan) dan nama entri memakai identifier tetap (DD-12) atau teks tetap (`2 TAGs`), sehingga semua asersi entri baru memakai selisih total terhadap baseline yang dicatat sebelum aksi (S-12); blok TC-267 memakai `N0`, `A0`, `B`, dan `C`, blok TC-268 memakai `N1` dan `A1`.
- Kemampuan teknis: pembaca nilai footer pagination Event Log dan Activity Log.
- State global yang diubah: tidak ada selain data (Seed Registri A dan log).

## Test Steps

### Baseline

1. Klik tombol `Event Log` di toolbar, catat total `N0` pada footer Tab Activate TAG (`Showing ... of N0 logs`), lalu tutup modal lewat `✕`
2. Buka Global Settings > Activity Log, tab User Action, filter Action `Delete TAG`, catat total entri `A0` pada footer
3. Ketik Search `E2801160600002054D8A0012`, tekan Enter, catat total entri `B` (0 bila empty state `No results found`), lalu klik `(←)` pada kotak Search
4. Ketik Search `2 TAGs`, tekan Enter, catat total entri `C` (0 bila empty state `No results found`), lalu klik `(←)` pada kotak Search

### TC-GS-TAG-267: Delete single mencatat Event Log dan Activity Log dengan kode tag dan entry point

5. Buka Global Settings > TAG, Tab All, ketik Search `E2801160600002054D8A0012`, tekan Enter
6. Buka menu baris DD-12, klik `Delete`, lalu konfirmasi dengan klik `Delete` pada dialog
7. Tunggu aksi selesai
8. Buka Event Log, Tab Activate TAG
9. Verifikasi total log menjadi `N0 + 1`
10. Verifikasi baris pertama (Date terbaru): Activity `Delete`, TAG Type `RFID`, Success `1`, Waiting for Approval `—`, Failed `0`, Hardware `—`
11. Tutup modal lewat `✕`, buka Global Settings > Activity Log, tab User Action, filter Action `Delete TAG`
12. Verifikasi total entri menjadi `A0 + 1`
13. Ketik Search `E2801160600002054D8A0012`, tekan Enter
14. Verifikasi total entri menjadi `B + 1`
15. Verifikasi entri teratas: Action `Delete TAG`, Name `E2801160600002054D8A0012`, Field `Status`, Old Value `Available`, New Value `Deleted (Actions)`
16. Klik `(←)` pada kotak Search, lalu catat total entri `A1` pada footer
17. Buka Global Settings > TAG, Tab All, klik tombol `Event Log`, catat total `N1` pada footer Tab Activate TAG, lalu tutup modal lewat `✕`

### TC-GS-TAG-268: Bulk Delete mencatat satu entri dengan jumlah tag dan entry point, TAG Type Mixed

18. Buka Global Settings > TAG, klik Tab Not Paired, ketik Search `E28011606000020F00000001`, tekan Enter, lalu centang baris DD-15
19. Ganti isi kotak search dengan `AABBCCDDEE80`, tekan Enter, lalu centang baris DD-04
20. Pilih `Bulk Action` > `Delete`, lalu klik `Delete` pada dialog
21. Tunggu aksi selesai
22. Buka Event Log, Tab Activate TAG
23. Verifikasi total log menjadi `N1 + 1`
24. Verifikasi baris pertama (Date terbaru): Activity `Delete`, TAG Type `Mixed`, Success `2`
25. Tutup modal lewat `✕`, buka Global Settings > Activity Log, tab User Action, filter Action `Delete TAG`
26. Verifikasi total entri menjadi `A1 + 1`
27. Ketik Search `2 TAGs`, tekan Enter
28. Verifikasi total entri menjadi `C + 1`
29. Verifikasi entri teratas: Action `Delete TAG`, Name `2 TAGs`, Field `Status`, Old Value `—`, New Value `Deleted (Bulk Delete)`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec sama dengan sumber (267, 268). Kedua blok menghapus data (prinsip 5 bagian 3: aksi destruktif di akhir spec); tidak ada kasus lain di spec ini yang membutuhkan baris itu.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1 sampai 4, 16, 17 (baseline sebelum aksi pemicu, S-12), langkah 5, 18, 19 (mencari baris target dan memilih baris; seleksi bertahan antar Search diasersi spec 071, TC-217), langkah 7 dan 21 (Tunggu aksi selesai), langkah 8, 11, 22, 25 (pindah surface).
- Pembagian lintas spec: Delete single dan bulk sebagai fungsi ada di spec 046, 050, 052; spec ini hanya mengasersi pencatatan Event Log dan Activity Log.
- Temuan untuk QA:
  - Seeding dan reset Seed Registri A antar spec tidak didefinisikan di TC (Q-4); DD-12 dan DD-15 dihapus spec ini sehingga spec lain yang memakainya memerlukan fixture BE.
  - TC-267 dan TC-268 tidak menyebut kolom Object entri Activity Log; spec tidak mengasersinya.
  - TC-268 Expected a hanya menyebut TAG Type `Mixed` dan Success `2`; Waiting for Approval, Failed, dan Hardware baris Mixed tidak diasersi.

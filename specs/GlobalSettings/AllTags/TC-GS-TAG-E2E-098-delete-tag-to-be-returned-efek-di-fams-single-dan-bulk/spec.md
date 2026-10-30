---
id: TC-GS-TAG-E2E-098-delete-tag-to-be-returned-efek-di-fams-single-dan-bulk
title: "Delete: Tag To be Returned Keluar dari Tab To Be Returned FAMS (Single dan Bulk)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-TAG-144
  - TC-GS-TAG-371
coverage:
  web: automated
---

# Delete: Tag To be Returned Keluar dari Tab To Be Returned FAMS (Single dan Bulk)

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini menghapus data registri: Delete DD-07 pada TC-GS-TAG-144, lalu Bulk Delete DD-07 dan DD-15 pada TC-GS-TAG-371 sesudah Seed Registri A dipulihkan penuh lewat fixture BE (langkah 22).
- Akun aktor (ganti akun eksplisit; hasil di FAMS diasersi di sesi FAMS):
  - Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`, untuk Fixed Asset > TAG > To Be Returned. Akun pertama spec: login di hook `before` spec ini.
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`, untuk Global Settings > TAG (aksi Delete). Hook `after` mengembalikan sesi ke akun ini sebagai default suite.
- Layar awal: hook `beforeEach` membuka Fixed Asset > TAG > To Be Returned (akun pertama spec).
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`). Target hapus: DD-07 `E2801160600002054D8A0007` (To be Returned, tampil di Fixed Asset > TAG > To Be Returned; aset terakhir sudah tidak bertag DD-07) dan DD-15 `E28011606000020F00000001` (Filler Tag Available di seed; disetel To be Returned, Return Group `Gudang Pusat`, lewat fixture BE untuk TC-GS-TAG-371, dengan aset terakhir yang disediakan fixture BE karena seed tidak memuat aset untuk DD-15). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4).
- Pemulihan sebelum TC-GS-TAG-371 (langkah 22): fixture BE memulihkan Seed Registri A penuh (DD-07 kembali ada, kartu RFID – Object TAG `21 of 50`), lalu menyetel DD-07 dan DD-15 menjadi To be Returned (Return Group `Gudang Pusat`) dengan aset terakhir masing-masing. Dengan pemulihan penuh ini kartu `19 of 50` pada langkah 34 berlaku.
- Kemampuan teknis (disediakan tim FE/BE): seed dan reset idempotent Seed Registri A; penyetelan DD-07 dan DD-15 menjadi To be Returned beserta aset terakhir; pembacaan TAG Log tag yang sudah dihapus; pembacaan jumlah entri Event Log To Be Returned sebelum aksi (N tidak diturunkan dari seeding); pembacaan status dan Tagging aset terakhir. Langkah dan selektor Fixed Asset tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A idempotent lewat fixture BE; kembalikan Rows per page ke 10; sesi dikembalikan ke Total Control Client A.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data di atas dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-144: Delete tag To be Returned, keluar dari tab To Be Returned FAMS

1. Catat badge tab To Be Returned
2. Ketik Search `E2801160600002054D8A0007`, tekan Enter
3. Verifikasi DD-07 tampil di tab To Be Returned
4. Klik `Event Log`, catat jumlah entri, lalu tutup modal
5. Buka aset terakhir DD-07 di Fixed Asset, catat status dan Tagging aset
6. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab All
7. Buka menu baris DD-07, lalu klik `Delete`
8. Klik `Delete` pada dialog
9. Verifikasi toast sukses `Success, TAG has been deleted.`
10. Verifikasi baris DD-07 hilang dari registri
11. Ketik Search `E2801160600002054D8A0007`, tekan Enter
12. Verifikasi pencarian menampilkan `No results found`
13. Verifikasi seluruh TAG Log DD-07 ikut terhapus (pembacaan lewat fixture BE)
14. Ganti akun ke Admin FAMS, buka Fixed Asset > TAG > To Be Returned
15. Verifikasi badge tab berkurang 1 dari nilai yang dicatat
16. Ketik Search `E2801160600002054D8A0007`, tekan Enter
17. Verifikasi pencarian menampilkan `No results found` (DD-07 tidak ada lagi di tab To Be Returned)
18. Klik `Event Log`
19. Verifikasi Event Log To Be Returned tidak memuat entri untuk DD-07 dan jumlah entri sama dengan yang dicatat
20. Tutup modal Event Log, lalu buka aset terakhir DD-07 di Fixed Asset
21. Verifikasi status dan Tagging aset sama seperti sebelum Delete

### TC-GS-TAG-371: Bulk Delete dua tag To be Returned

22. Pulihkan Seed Registri A penuh lewat fixture BE dan setel DD-07 serta DD-15 menjadi To be Returned (Return Group `Gudang Pusat`) dengan aset terakhir, lalu buka ulang Fixed Asset > TAG > To Be Returned
23. Catat badge tab To Be Returned
24. Verifikasi DD-07 dan DD-15 tampil di tab To Be Returned
25. Klik `Event Log`, catat jumlah entri, lalu tutup modal
26. Buka aset terakhir DD-07 dan DD-15 di Fixed Asset, catat status dan Tagging aset masing-masing
27. Ganti akun ke Total Control Client A, buka Global Settings > TAG Tab Not Paired
28. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
29. Centang DD-07 dan DD-15, pilih `Bulk Action` > `Delete`
30. Klik `Delete` pada dialog
31. Verifikasi toast sukses `Success, TAG has been deleted.`
32. Verifikasi baris DD-07 dan DD-15 hilang dari registri
33. Klik Tab All
34. Verifikasi kartu RFID – Object TAG `19 of 50`
35. Ganti akun ke Admin FAMS, buka Fixed Asset > TAG > To Be Returned
36. Verifikasi DD-07 dan DD-15 tidak ada lagi di tab To Be Returned
37. Verifikasi badge tab berkurang 2 dari nilai yang dicatat
38. Klik `Event Log`
39. Verifikasi Event Log To Be Returned tidak memuat entri untuk DD-07 maupun DD-15 dan jumlah entri sama dengan yang dicatat
40. Tutup modal Event Log, lalu buka aset terakhir DD-07 dan DD-15 di Fixed Asset
41. Verifikasi status dan Tagging aset DD-07 dan DD-15 sama seperti sebelum Delete

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (41 langkah nominal). Alasan: dua TC satu topik aksi (Delete tag To be Returned dan efeknya di Fixed Asset) dengan satu dataset Seed Registri A; blok TC-GS-TAG-371 berdiri sendiri (Seed Registri A dipulihkan penuh di langkah 22 dan baseline dicatat ulang), dan bagian sesudah tiap ganti akun tetap bermakna walau bagian sebelumnya gagal. Mayoritas langkah adalah ganti akun dan navigasi ke Fixed Asset yang dibutuhkan Expected TC.
- Pemisahan: spec ini memuat seluruh blok FAMS (kelas harness FE+BE dengan fixture aset terakhir dan akun Admin FAMS); TC-GS-TAG-145, 187, dan 347 (Approvals dan Admin Console TAG Stock) ada di spec 051.
- Langkah ganti akun eksplisit: 6, 14, 27, 35.
- Perubahan urutan (S-05 butir terakhir): pada TC-GS-TAG-144, asersi registri Global Settings (baris hilang, `No results found`, TAG Log; langkah 10 sampai 13) ditaruh tepat sesudah Delete, sebelum kembali ke FAMS (langkah 14 sampai 21), supaya ganti akun tidak berulang. TC-GS-TAG-371 ditaruh sesudah TC-GS-TAG-144 karena memakai DD-07 yang sudah dihapus TC-GS-TAG-144 dan dipulihkan di langkah 22.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1, 4, 5, 23, 25, dan 26 (mencatat baseline badge, jumlah entri Event Log, atau status aset), 2 (Search agar baris DD-07 tampil), 6, 14, 20, 27, 33, 35, dan 40 (ganti akun dan navigasi; langkah 33 klik Tab All karena kartu `N of M` hanya tampil di Tab All), 22 (memulihkan data lewat fixture BE), 28 (mengubah Rows per page menjadi 50 supaya DD-07 dan DD-15 yang berada di halaman 2 Tab Not Paired tampil dan dapat dicentang; dikembalikan ke 10 di hook `after`).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 (anchor positif sebelum absence, S-02 butir 2 bagian 8b; langkah 24 adalah langkah 1 TC-GS-TAG-371 sehingga bukan tambahan); langkah 9 dan 31 memakai toast `Success, TAG has been deleted.` yang ditetapkan TC-GS-TAG-142 sebagai teks toast Delete tag.
- Pengecualian P-1 (state berat): asersi bahwa Event Log To Be Returned tidak memuat entri DD-07 dan jumlah entri tetap (langkah 19), serta DD-07 dan DD-15 (langkah 39), memakai baseline jumlah entri yang dicatat sebelum Delete (langkah 4 dan 25; S-05, S-12) dan didahului toast sukses (langkah 9 dan 31) serta badge tab berkurang (langkah 15 dan 37) sebagai anchor positif (bagian 8b butir 2); state berat (penghapusan tag To be Returned dengan aset terakhir) dibangun di spec ini.
- Rujukan: TC-GS-TAG-358 (Delete by Scan atas DD-07 dengan verifikasi FAMS) ada di spec 099.
- Temuan untuk QA:
  - Q-9: langkah dan selektor di Fixed Asset tidak didefinisikan; verifikasi di FAMS hanya sejauh Expected TC.
  - TC-GS-TAG-371 mensyaratkan DD-15 To be Returned lewat fixture BE dan Expected d menyebut "aset terakhir keduanya", tetapi tidak menyebut aset terakhir DD-15 di Data Uji; DD-15 di Seed Registri A adalah Filler Tag tanpa aset, sehingga fixture BE menyediakan aset terakhir DD-15 (S-15).
  - Post Condition TC-GS-TAG-144 butir b dan c identik dengan Expected c dan d. Post Condition TC-GS-TAG-371 butir a dan b identik dengan Expected a dan b; butir c ("Satu baris Event Log Delete di Global Settings (Success 2)") tidak punya langkah observasi di TC dan tidak diasersi.
  - Q-4: identifier tetap; kartu `19 of 50` valid karena Seed Registri A dipulihkan penuh sebelum TC-GS-TAG-371 (langkah 22).

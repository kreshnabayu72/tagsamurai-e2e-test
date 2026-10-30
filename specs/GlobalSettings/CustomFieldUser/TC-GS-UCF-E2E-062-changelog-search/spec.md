---
id: TC-GS-UCF-E2E-062-changelog-search
title: "Modal Changelog Custom Field: Search, Siklus Search Toolbar, Kolom Teks, Date Tidak Dicari, Kolom Hidden Dikecualikan, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-258
  - TC-GS-UCF-516
  - TC-GS-UCF-259
  - TC-GS-UCF-260
  - TC-GS-UCF-517
  - TC-GS-UCF-256
coverage:
  web: automated
---

# Modal Changelog Custom Field: Search, Siklus Search Toolbar, Kolom Teks, Date Tidak Dicari, Kolom Hidden Dikecualikan, dan Empty State

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka.
- Data Pre-setup (baca-saja, tidak diubah spec ini): 6 Custom Field Pre-setup Client A dan Changelog Pre-setup 8 entri bertanggal 8 sampai 11 Sep 2026 (fixture backend): Edit `Cost Center` Value Setting (Budi S), Create `Cost Center` (Budi S), Activate `Employee Grade` (Siti R), Deactivate `Joining Date` (Budi S), Delete `Legacy Field` (Siti R), Create `Job Description` (Siti R), Create `Bonus` (Budi S), Create `Office Phone` (Budi S).
- Data Population (precondition TC): 8 Custom Field Population dibuat lewat API oleh Sari Dewi di hook `before` bila belum ada (seeding idempotent; menghasilkan 8 entri Create dengan Modified By `Sari D`); dipakai sebagai precondition TC, tidak diasersi satu per satu.
- General Settings Client A: Date Format `DDD, MMM dd, yyyy`, Time Format `hh:mm a` (nilai default fixture, tidak diubah spec ini). Dipakai TC-GS-UCF-260 untuk menyusun teks tanggal.
- Setup Column Modal Changelog: konfigurasi default (6 kolom terlihat, urutan default, tanpa pin); hook `beforeEach` membersihkan cache browser. TC-GS-UCF-259 dan 517 menyembunyikan lalu menampilkan kembali kolom `Field`; hook `after` menjalankan `[Reset to Default]` sebagai cadangan.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: hover untuk tooltip; mengetik dan Enter pada Search Modal Changelog.
- State global: tidak ada yang diubah selain flag Guided Tooltip dan konfigurasi Setup Column Changelog (dipulihkan seperti di atas).

## Test Steps

### TC-GS-UCF-258: Placeholder Search Modal Changelog

1. Klik icon Changelog
2. Klik icon Search
3. Verifikasi placeholder `Search changelog...`
4. Klik `(←)` pada kotak Search

### TC-GS-UCF-516: Siklus Search toolbar Modal Changelog

5. Hover icon Search
6. Verifikasi tooltip `Search`
7. Klik icon Search
8. Verifikasi Search melebar
9. Verifikasi fokus otomatis di kotak Search
10. Verifikasi placeholder `Search changelog...`
11. Ketik `Legacy`
12. Verifikasi `(✕)` muncul
13. Verifikasi tabel belum tersaring (sedikitnya satu entri selain Delete `Legacy Field` masih tampil)
14. Tekan Enter
15. Verifikasi entri Delete `Legacy Field` tampil
16. Verifikasi tabel hanya memuat entri Delete `Legacy Field`
17. Klik `(✕)`
18. Verifikasi input Search kosong
19. Verifikasi tabel masih menampilkan entri Delete `Legacy Field`
20. Tekan Enter
21. Verifikasi entri kembali lengkap (10 entri pada halaman 1)
22. Ketik `Legacy`, tekan Enter, lalu klik `(←)`
23. Verifikasi Search tertutup
24. Verifikasi tabel langsung reset (10 entri pada halaman 1)

### TC-GS-UCF-259: Search Changelog kelas kolom teks

25. Ketik Search `Deactivate`, tekan Enter
26. Verifikasi entri Deactivate `Joining Date` tampil (kolom Action)
27. Ganti isi kotak search dengan `Value Setting`, tekan Enter
28. Verifikasi entri Edit `Cost Center — Value Setting` tampil (kolom Field)
29. Ganti isi kotak search dengan `Marketing`, tekan Enter
30. Verifikasi entri Edit `Cost Center` dengan New Value memuat `Marketing` tampil (kolom New Value)
31. Klik header Column Visibility (⋯), uncheck `Field`
32. Ganti isi kotak search dengan `Legacy`, tekan Enter
33. Verifikasi entri Delete `Legacy Field` tetap ditemukan lewat Old Value `Legacy Field` dengan kolom `Field` hidden (kolom Old Value)
34. Klik header Column Visibility (⋯), centang kembali `Field`
35. Verifikasi kolom `Field` ditampilkan kembali
36. Ganti isi kotak search dengan `siti`, tekan Enter
37. Verifikasi entri Activate `Employee Grade` tampil (kolom Modified By)
38. Verifikasi entri Delete `Legacy Field` tampil (kolom Modified By)
39. Verifikasi entri Create `Job Description` (Modified By `Siti R`) tampil (kolom Modified By)

### TC-GS-UCF-260: Search nilai Date tidak mencocokkan baris

40. Ganti isi kotak search dengan teks tanggal entri Create `Cost Center` sesuai Date Format General Settings (bagian tanggal `DDD, MMM dd, yyyy`), tekan Enter
41. Verifikasi Title `No results found`

### TC-GS-UCF-517: Kolom hidden dikecualikan dari Search dan kembali dicari setelah unhide

42. Ganti isi kotak search dengan `Value Setting`, tekan Enter
43. Verifikasi entri Edit `Cost Center — Value Setting` tampil
44. Verifikasi tabel hanya memuat entri Edit `Cost Center — Value Setting`
45. Klik header Column Visibility (⋯), uncheck `Field`
46. Kosongkan input Search, ketik `Value Setting`, tekan Enter
47. Verifikasi empty state `No results found` (kolom `Field` tidak dicari)
48. Klik header Column Visibility (⋯), centang kembali `Field`
49. Kosongkan input Search, ketik `Value Setting`, tekan Enter
50. Verifikasi entri Edit `Cost Center — Value Setting` kembali ditemukan
51. Klik `(←)` pada kotak Search

### TC-GS-UCF-256: Empty state saat Search tidak menemukan hasil

52. Ketik Search `zzqx`, tekan Enter
53. Verifikasi Title `No results found`
54. Verifikasi Description `Try adjusting your search or filter.`
55. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 258, 516, 259, 260, 517, 256. Modal dibuka sekali (langkah 1) dan seluruh kasus Search berjalan pada pembukaan itu; modal ditutup sekali (langkah 55). Urutan ini menyimpang dari urutan TC sumber: kasus yang memakai Setup Column (259, 517) mengembalikan kolom `Field` sebelum kasus berikutnya; empty state (256) di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal), langkah 4 dan 51 (menutup kotak Search lewat `(←)` supaya kasus berikutnya dimulai dengan Search tertutup dan tabel reset), langkah 31, 34, 45, 48 (mengubah visibility kolom `Field`; pemulihan dicatat dengan `Verifikasi` kolom di langkah 35), langkah 46 dan 49 (mengosongkan input lalu mengetik ulang, sesuai langkah TC-GS-UCF-517), langkah 55 (menutup modal lewat `[✕]`; modal tidak memuat form sehingga tanpa dialog).
- Langkah 11, 14, 22 dan seterusnya menulis Search sebagai satu langkah atomik sesuai bagian 8b butir 9; langkah 5 sampai 7 (siklus input) dipertahankan terpisah karena TC-GS-UCF-516 menguji siklus input.
- Asersi "hanya entri ..." (langkah 16 dan 44) didahului `Verifikasi` entri yang dicari tampil (langkah 15 dan 43) sebagai pembanding, dan empty state langkah 47 dan 53 adalah anchor positif bagi hasil Search kosong (bagian 8b butir 2).
- Langkah 13 membuktikan tabel belum tersaring sebelum Enter dengan entri lain yang masih tampil.
- Spec melewati sekitar 35 langkah (55 langkah). Seluruhnya satu kelas ringan (Search Modal Changelog, hanya membaca, satu dataset Pre-setup), dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Topik satu dataset Changelog dipertahankan sebagai spec terpisah (lihat Notes spec 061).
- Temuan untuk QA:
  - TC-GS-UCF-516 Expected e menyebut "10 entri pada halaman 1" yang bergantung pada Changelog Client A berisi sedikitnya 10 entri (16 menurut precondition); tidak bergantung pada total persis.
  - TC-GS-UCF-259 langkah 8 dan Expected e: Search `siti` diasersi pada tiga entri Pre-setup; entri lain yang Modified By-nya memuat `siti` (mis. data spec lain) bisa ikut tampil. Spec hanya mengasersi kehadiran ketiga entri Pre-setup.
  - TC-GS-UCF-260 langkah 2 menyebut "teks tanggal salah satu entri" tanpa menyebut entri; spec memakai bagian tanggal entri Create `Cost Center` (Pre-setup, 11 Sep 2026) dalam Date Format `DDD, MMM dd, yyyy`.
  - TC-GS-UCF-517 Expected a "hanya entri Edit `Cost Center — Value Setting`" mengasumsikan tidak ada entri Changelog lain dengan Field memuat `Value Setting`; entri spec lain di Client A (mis. rename atau tambah value Dropdown) dapat membuat asersi ini gagal bila lingkungan tidak bersih.

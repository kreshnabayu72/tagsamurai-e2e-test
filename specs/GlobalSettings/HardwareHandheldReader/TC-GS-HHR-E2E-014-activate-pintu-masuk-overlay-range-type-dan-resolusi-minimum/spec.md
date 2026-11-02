---
id: TC-GS-HHR-E2E-014-activate-pintu-masuk-overlay-range-type-dan-resolusi-minimum
title: "Pintu Masuk Activate Reader: Overlay Select Range Type, Penutupan Overlay, Popup Menunggu Sync, dan Resolusi Minimum 1280x720"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-51
  - TC-GS-HHR-52
  - TC-GS-HHR-53
  - TC-GS-HHR-57
  - TC-GS-HHR-444
coverage:
  web: automated
---

# Pintu Masuk Activate Reader: Overlay Select Range Type, Penutupan Overlay, Popup Menunggu Sync, dan Resolusi Minimum 1280x720

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memakai simulator reader USB bersama, mengubah ukuran viewport, dan memakai Seed Reader A serta kuota Client A yang dipakai spec lain.
- Aktor: Total Control Sari Dewi (Client A) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader; hook `after` mengembalikan sesi ke akun default suite (akun yang sama).
- Flag Guided Tooltip `guided_tooltip_seen_gs-handheld-reader` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji `tc-hardware-handheld-reader.md`): Client A plan Growth, Seed Reader A DD-01 s.d. DD-10 (kartu `Short Range` `5 of 8`, kartu `Long Range` `5 of 6`), format tanggal default General Settings. Hardware Stock Principal: HS-01 (`SN-HHR-00201`, Long Range, Zebra/RFD40, Current Power 22 dBm) dan HS-02 (`SN-HHR-00202`, Short Range). State awal dipulihkan oleh fixture backend sebelum spec (Catatan TC; mekanisme disediakan tim FE/BE).
- Spec tidak mengirim `[Submit]` aktivasi: tidak ada reader, log, atau perubahan stok yang dibuat, sehingga tidak ada data Pre-setup yang perlu dipulihkan.
- Kemampuan teknis:
  - Simulator reader USB dan driver lokal yang menyajikan reader tersambung dengan Serial Number tertentu (`SN-HHR-00202` Short Range, `SN-HHR-00201` Long Range) untuk langkah `[Sync]`; disediakan tim FE (mekanisme tidak didefinisikan di TC, PRD, atau LLD; lihat Temuan untuk QA). TC-GS-HHR-53 dan TC-GS-HHR-57 berlabel Manual Only (b) di TC sumber.
  - Kontrol ukuran viewport (1280x720) dan pemulihannya.
  - Pembacaan posisi dan ukuran elemen (overlay menempel di bawah tombol, checkbox tepat di atas `[Submit]`, elemen tidak terpotong, elemen dapat diklik).
- Cleanup (hook `after`, tidak berasumsi spec berjalan penuh): tutup overlay atau popup yang masih terbuka dan pulihkan viewport ke ukuran awal.

## Test Steps

### TC-GS-HHR-51: Overlay Select Range Type tampil di bawah tombol Activate Reader

1. Klik `[+ Activate Reader]`
2. Verifikasi Overlay `Select Range Type` menempel di bawah tombol `[+ Activate Reader]`
3. Verifikasi overlay bukan dialog: tanpa backdrop dan tanpa tombol konfirmasi
4. Verifikasi overlay memuat dua pilihan: `Short Range` dan `Long Range`
5. Verifikasi sisa kuota tidak ditampilkan di overlay

### TC-GS-HHR-444: Overlay ditutup oleh Esc dan klik di luar overlay tanpa efek lain

6. Tekan `Esc`
7. Verifikasi Overlay `Select Range Type` tertutup
8. Verifikasi Popup `Activate Handheld Reader` dan dialog apa pun tidak terbuka
9. Klik `[+ Activate Reader]` lagi
10. Klik area di luar overlay
11. Verifikasi Overlay `Select Range Type` tertutup tanpa efek lain
12. Verifikasi Popup `Activate Handheld Reader` dan dialog apa pun tidak terbuka
13. Verifikasi kartu `Short Range` tetap `5 of 8`
14. Verifikasi kartu `Long Range` tetap `5 of 6`

### TC-GS-HHR-52: Memilih Long Range dengan kuota tersedia membuka Popup Activate

15. Klik `[+ Activate Reader]`
16. Klik `Long Range` pada Overlay `Select Range Type`
17. Verifikasi Overlay `Select Range Type` tertutup
18. Verifikasi Popup `Activate Handheld Reader` terbuka langsung dengan Range Type `Long Range`
19. Verifikasi header popup berisi ikon `[✕]`
20. Verifikasi instruksi `Connect the reader via USB cable, then click Sync.` tampil
21. Verifikasi tombol `[Sync]` tampil
22. Verifikasi footer `[Clear Field]` dan `[Submit]` tampil dan keduanya disabled
23. Verifikasi tombol `[Cancel]` tidak ada
24. Verifikasi checkbox `Stay on this form after submitting` tampil tepat di atas `[Submit]`
25. Verifikasi checkbox `Stay on this form after submitting` tidak tercentang
26. Verifikasi sebelum Sync hanya instruksi, checkbox `Stay on this form after submitting`, `[Sync]`, `[Clear Field]`, dan `[Submit]` (disabled) yang tampil
27. Verifikasi `Serial Number`, label jalur, `Device Name`, `SKU`, `Brand`, `Model/Type`, slider `Reader Power`, dan `Alias Name` belum tampil

### TC-GS-HHR-53: Memilih Short Range membuka Popup Activate tanpa kontrol Reader Power

28. Klik `[✕]` di header popup
29. Klik `[+ Activate Reader]`
30. Klik `Short Range` pada Overlay `Select Range Type`
31. Verifikasi Popup `Activate Handheld Reader` terbuka dengan Range Type `Short Range`
32. Sambungkan reader Short Range dengan Serial Number `SN-HHR-00202` (HS-02) lewat simulator reader USB
33. Klik `[Sync]`
34. Verifikasi `Serial Number` read-only terisi `SN-HHR-00202` (Sync berhasil)
35. Verifikasi slider `Reader Power` tidak ada pada popup Short Range
36. Klik `[✕]` di header popup
37. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
38. Klik `[Cancel Activation]`

### TC-GS-HHR-57: Popup Activate dapat dipakai penuh pada resolusi minimum 1280x720

39. Atur viewport browser ke 1280x720
40. Klik `[+ Activate Reader]`
41. Klik `Long Range` pada Overlay `Select Range Type`
42. Sambungkan reader Long Range dengan Serial Number `SN-HHR-00201` (HS-01) lewat simulator reader USB
43. Klik `[Sync]`
44. Verifikasi seluruh elemen popup (header `[✕]`, `[Sync]`, `Serial Number`, label `Official`, slider `Reader Power`, `Alias Name`, `[Clear Field]`, `[Submit]`) terlihat tanpa terpotong
45. Verifikasi seluruh elemen popup yang sama dapat diklik
46. Klik `[✕]` di header popup
47. Verifikasi dialog `Cancel Activation` tampil dengan body "Are you sure you want to cancel this activation? The Sync progress you've made will be lost." dan tombol `[Go Back]` `[Cancel Activation]`
48. Klik `[Cancel Activation]`
49. Pulihkan viewport browser ke ukuran awal

## Notes

- Mode: FE+BE. Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md`. Spec memuat dua kelas harness: screening fungsional (TC-GS-HHR-51, TC-GS-HHR-444, TC-GS-HHR-52) dan harness eksternal simulator reader USB (TC-GS-HHR-53 dan TC-GS-HHR-57). Keduanya berbagi topik pintu masuk Activate, akun, dan data yang sama; blok USB diletakkan di akhir spec supaya kegagalan simulator tidak menutupi hasil blok screening.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (49 langkah). Alasan: 28 langkah adalah `Verifikasi` yang dipecah satu per klausa Expected (S-01), terutama TC-GS-HHR-52 (11 langkah `Verifikasi` untuk tujuh butir Expected) dan TC-GS-HHR-444 (6 langkah); seluruh blok memakai satu topik (pintu masuk popup Activate), satu akun, dan data yang sama, tidak membuat data, dan blok screening berjalan lebih dulu sehingga kegagalan TC-GS-HHR-53 atau TC-GS-HHR-57 tidak menghapus hasil blok sebelumnya.
- Langkah penghubung (tanpa `Verifikasi`): langkah 28 menutup popup TC-GS-HHR-52 yang belum berisi hasil Sync agar TC-GS-HHR-53 membuka popup baru (TC-GS-HHR-62 menutup popup tanpa hasil Sync lewat `[✕]` tanpa dialog); langkah 32 dan 42 menyiapkan reader di simulator; langkah 36 sampai 38 dan 46 sampai 48 menutup popup yang sudah berisi hasil Sync lewat dialog `Cancel Activation` (S-08); langkah 39 dan 49 mengatur dan memulihkan viewport.
- Teks dialog `Cancel Activation` (langkah 37 dan 47) mengikuti Expected TC-GS-HHR-89; TC-GS-HHR-53 dan TC-GS-HHR-57 sendiri tidak memuatnya.
- Langkah 34 adalah `Verifikasi` tambahan di luar Expected TC-GS-HHR-53 yang menjadi anchor positif (Sync berhasil) bagi asersi absence slider `Reader Power` pada langkah 35 (butir 2 bagian 8b konvensi); langkah 7 dan 11 menjadi anchor bagi absence popup dan dialog pada langkah 8 dan 12.
- Tidak ada pencatatan log yang diasersi di spec ini.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB, driver lokal, dan pembacaan Serial Number tidak didefinisikan di TC, PRD, atau LLD (TC-GS-HHR-53 dan TC-GS-HHR-57 berlabel Manual Only (b)); spec hanya mencatat kebutuhan di Prerequisites dan tidak mengarang endpoint atau perintah simulator.
  - TC-GS-HHR-57 tidak mendefinisikan cara mengukur "terpotong" dan "dapat diklik" pada viewport 1280x720; spec memecahnya menjadi dua `Verifikasi` (langkah 44 dan 45) dan membutuhkan pembacaan geometri elemen (Prerequisites).
  - TC-GS-HHR-53 tidak menyebut kuota atau stok yang dikonsumsi (tidak ada Submit); spec tidak mengirim `[Submit]` pada TC mana pun sehingga stok HS-01 dan HS-02 tidak berubah.

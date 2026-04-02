import { createApp, ref, h, onMounted } from 'vue'
import Dialog from '@/components/common/Dialog.vue'

interface Options {
    context: string,
    onConfirm?: Function,
    onCancel?: Function
}

export const showDialog = (options: Options) => {
    // 创建挂载点
    const container = document.createElement('div')
    document.body.appendChild(container)

    // 实例化App对象
    const dialogApp = createApp({
        setup() {
            const visible = ref<boolean>(false)

            onMounted(() => {
                setTimeout(() => visible.value = true, 50)
            })

            const handleClose = () => {
                visible.value = false
                setTimeout(() => {
                    dialogApp.unmount()
                    container.remove()
                }, 300)
            }

            return () => h(Dialog, {
                visible: visible.value,
                onClose: handleClose,
                context: options.context,
                onConfirm: options.onConfirm,
                onCancel: options.onCancel
            })
        }
    })

    // 挂载App对象
    dialogApp.mount(container)
}